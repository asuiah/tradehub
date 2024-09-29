from abc import ABC, abstractmethod


class TransformerAbstract(ABC):
    @abstractmethod
    def process_data(self, data):
        """处理市场数据"""
        pass
