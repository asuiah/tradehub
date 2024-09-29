import yfinance as yf


from ..interface import MarketFetcherBase
from .interface import YahooAPIConfig


class Yahoo(MarketFetcherBase):
    def __init__(self, config: YahooAPIConfig) -> None:
        self.config = config

    def update_config(self, config: YahooAPIConfig):
        self.config = {**self.config, **config}

    def fetch_data(self):
        data = yf.download(**self.config)
        return data

    def process_data(self, data):
        return super().process_data(data)
