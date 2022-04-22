import os
import json
import logging
import requests

from tqdm import tqdm
from typing import List
from pathlib import Path
from dataclasses import dataclass
from datetime import date, timedelta, datetime

from .exceptionetl import FailResponse
from utils.constants import data_dir, URL_COIN, PING, COIN_FILE_PATH_DUMP
from utils.postgres_utils import insert_values_to_table
from .sql.template_query import insert_coin_data

# Logging set up
logger = logging.getLogger(__name__)
formatter = "%(asctime)s - %(levelname)s: %(message)s"
logging.basicConfig(format=formatter)
logger.setLevel(10)

DS_FORMAT = '%Y-%m-%d'
CURRENT_DATE = datetime.now().strftime(DS_FORMAT)


@dataclass
class DataCollect:
    """Data class
    Fetch data related to a crypto currency from www.coingecko.com API and
    then ingest the data base with it.
    """
    coin: str

    def is_up(self) -> bool:
        """Return true if the API is up."""
        r = requests.get(PING)
        return True if r.status_code == 200 else False


    def get_bulk_data(self, d_from: str, d_to: str):
        dates = self._get_all_dates(d_from , d_to)
        coin_dump_path = Path(data_dir,self.coin)
        os.makedirs(coin_dump_path, exist_ok=True)

        for current_date in tqdm(dates, desc='Processing the bulk dates'):
            logger.info(f'=== Getting info of {self.coin} and date {current_date}===')

            try:
                r = requests.get(URL_COIN.format(COIN=self.coin, DATE=current_date.strftime("%d-%m-%Y")))
                if r.status_code == 200:
                    json.dump(r.json(),
                            open(Path(coin_dump_path, COIN_FILE_PATH_DUMP.format(CRYPTO=self.coin, DATE=current_date)), "w"),
                            indent=4, separators=(',', ': '))
                    logger.info('=== Crypto data saved at: %s ===', coin_dump_path)
                else:
                    raise FailResponse(f'Something went wrong trying to fetch the data. Error:{ERROR}'.format(ERROR=r.text))

            except ValueError as error:
                message = "Error '%s' while try to fetch the crypto data"
                logger.error(message, error)
                raise FailResponse(error)


    def _get_all_dates(self, d_from , d_to) -> list:
        """Return a list with all the dates between two dates.
        At this moment there are not any validation such as if the start date is small than the second one.
        """
        start_date =  datetime.strptime(d_from, '%d-%m-%Y')
        end_date = datetime.strptime(d_to, '%d-%m-%Y')

        delta = end_date - start_date
        dates_to_fetch = [start_date + timedelta(days=x) for x in range(delta.days+1)]

        return dates_to_fetch


@dataclass
class DataDump:
    coin: str

    def dump_data_to_db(self):
        coin_dir = Path(data_dir,self.coin)

        for j_file in tqdm(self.yield_coin_files(coin_dir), desc='Saving criptos to db'):
            line = (j_file.get('symbol'), j_file.get('market_data')['current_price']['usd'], CURRENT_DATE, json.dumps(j_file))
            insert_values_to_table(insert_coin_data, line)
            logger.info('=== Saved row ===')

    def yield_coin_files(self, coin_dir: Path):
        for coin_json in os.listdir(coin_dir):
            if coin_json.endswith('.json'):
                with open(Path(coin_dir,coin_json)) as f:
                    yield json.load(f)
