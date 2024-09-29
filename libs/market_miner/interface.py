from abc import ABC, abstractmethod
from typing import Dict, Union


class MarketFetcherBase(ABC):
    @abstractmethod
    def update_config(self, config: Dict[str, Union[str, int, Dict]]):
        """更新配置"""
        pass

    @abstractmethod
    def fetch_data(self, config: Dict[str, Union[str, int, Dict]]):
        """获取市场数据"""
        pass

    @abstractmethod
    def process_data(self, data):
        """处理市场数据"""
        pass
