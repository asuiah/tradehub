from typing import Union, Literal
import pandas as pd

from .yahoo import Yahoo, YahooAPIConfig
from .transformer import TransformerAbstract
from .interface import MarketFetcherBase


class MarketMiner:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(
        self,
        privoder_name: Literal["YAHOO"],
        provider_config: Union[YahooAPIConfig] = {},
    ) -> None:
        self._fetcher = self._get_fetcher_by_provider(privoder_name, provider_config)
        self._fetcher = self._get_fetcher_by_provider(privoder_name, provider_config)

    def update_fetcher_config(self, fetcher_config: Union[YahooAPIConfig]):
        self._fetcher.update_config(fetcher_config)

    def fetch_data(self):
        return self._fetcher.fetch_data()

    # TODO: 根据需求再添加应用细节
    def process_data(
        self,
        transformer: TransformerAbstract,
        data: pd.DataFrame,
    ):
        transformedData = transformer.process_data(data)
        return transformedData

    def _get_fetcher_by_provider(
        self,
        resource_proider_name: Literal["YAHOO"],
        provider_config: Union[YahooAPIConfig] = {},
    ) -> MarketFetcherBase:
        if resource_proider_name == "YAHOO":
            return Yahoo(config=provider_config)


if __name__ == "__main__":
    yahooFetcherConfig: YahooAPIConfig = {
        "tickers": ["AAPL"],
        "period": "1d",
        "start": "2024-08-26",
        "end": "2024-08-27",
        "interval": "1m",
        "prepost": False,
    }
    fetcher = MarketMiner(privoder_name="YAHOO", provider_config=yahooFetcherConfig)
    fetcher.update_fetcher_config(yahooFetcherConfig)
    data = fetcher.fetch_data()
    print(data)
