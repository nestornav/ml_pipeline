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

# Logging set up
logger = logging.getLogger(__name__)
formatter = "%(asctime)s - %(levelname)s: %(message)s"
logging.basicConfig(format=formatter)
logger.setLevel(10)

CURRENT_DATE = datetime.now().strftime("%Y%m%d")



@dataclass
class Data:
    """Data class
    Fetch data related to a crypto currency from www.coingecko.com API and
    then ingest the data base with it.
    """
    coin: str

    def is_up(self):
        """Return the information if the API is up or not."""
        r = requests.get(PING)
        return True if r.status_code == 200 else False


    def get_bulk_data(self, d_from: str, d_to: str):
        dates = self._get_all_dates(d_from , d_to)
        os.makedirs(data_dir, exist_ok=True)

        for current_date in tqdm(dates, desc='Processing the bulk dates'):
            logger.info(f'=== Getting info of {self.coin} and date {current_date}===')

            try:
                r = requests.get(URL_COIN.format(COIN=self.coin, DATE=current_date.strftime("%d-%m-%Y")))
                if r.status_code == 200:
                    json.dump(r.json(),
                            open(Path(data_dir, COIN_FILE_PATH_DUMP.format(CRYPTO=self.coin, DATE=current_date)), "w"),
                            indent=4, separators=(',', ': '))
                    logger.info('=== Crypto data saved at: %s ===', data_dir)
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
