import typing
from abc import ABC, abstractmethod
from .moomoo.interface import FTModifyOrderConfig
import pandas as pd


class BrokerResponseBase(typing.TypedDict):
    code: int


class BrokerSuccessResponse(BrokerResponseBase):
    data: object


class BrokerErrorResponse(BrokerResponseBase):
    errors: object


RetCode: typing.TypeAlias = int
ErrorMessage: typing.TypeAlias = str
RetData: typing.TypeAlias = tuple[RetCode, pd.DataFrame | ErrorMessage]


class BrokerStrategy(ABC):

    @abstractmethod
    def close(self) -> RetData:
        """关闭Broker"""
        pass

    @abstractmethod
    def get_account_info(self) -> RetData:
        """获取当前账户信息"""
        pass

    @abstractmethod
    def sell_stock(self, code: str, sell_price: float, qty: int) -> RetData:
        """卖出下单"""
        pass

    @abstractmethod
    def buy_stock(self, code: str, buy_price: float, qty: int) -> RetData:
        """买入下单"""
        pass

    @abstractmethod
    def modify_order(self, params: FTModifyOrderConfig) -> RetData:
        """修改订单"""
        pass

    @abstractmethod
    def cancel_order(self, order_id: str) -> RetData:
        """取消订单"""
        pass

    @abstractmethod
    def get_order_list(self, start_date: str, end_date: str) -> RetData:
        """获取订单列表"""
        pass

    @abstractmethod
    def get_position_list(self) -> RetData:
        """获取持仓列表"""
        pass
