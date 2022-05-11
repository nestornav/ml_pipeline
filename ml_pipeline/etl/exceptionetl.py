class ETLException(Exception):
    pass

class FailResponse(ETLException):
    pass

class CoinGeckoDownException(ETLException):
    pass
