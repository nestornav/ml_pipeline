import os

from pathlib import Path

# | Directories (don't touch)
work_dir = str(Path(os.path.dirname(__file__)).parent)
data_dir = Path(work_dir, 'data')
sql_dir = Path(work_dir, 'etl/sql')

COIN_FILE_PATH_DUMP = '{CRYPTO}_data_{DATE}.json'
TABLES_FILE_NAME = 'tables_creation.sql'

# Crypto API
PING = 'https://api.coingecko.com/api/v3/ping'
URL_COIN = 'https://api.coingecko.com/api/v3/coins/{COIN}/history?date={DATE}&localization=false'
