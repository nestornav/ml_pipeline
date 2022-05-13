import typer

from ..data import DataCollect, DataDump
from .exceptionetl import CoinGeckoDownException

app = typer.Typer()

@app.command()
def get_coin_data(date_from: str, date_to: str):
    collect = data.DataCollect()
    if collect.is_up():
        typer.echo(f'from:{date_from}')
    else:
        raise CoinGeckoDownException('API is down, try later')

if __name__ == "__main__":
    app()
