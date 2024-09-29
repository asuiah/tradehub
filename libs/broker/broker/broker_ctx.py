from .interface import BrokerStrategy, RetData
from .constant import RET_CODE, TradeEnum
from .moomoo.interface import FTModifyOrderConfig
from .interface import RetCode
import pandas as pd


class BrokerCtx:
    def __init__(
        self,
        broker: BrokerStrategy,
    ) -> None:
        self._broker = broker

    def get_broker(self) -> BrokerStrategy:
        return self._broker

    def set_broker(self, broker: BrokerStrategy) -> None:
        self._broker = broker

    def trade(self, code: str, price: float, qty: int, trade_type: str) -> RetData:
        """
        交易订单

        code: 股票交易代码 (MooMoo 美股需添加 prefix US. 例如 SOUN => US.SOUN )
        price: 成交价格
        qty: 成交数量
        trade_type: 交易类型(TradeEnum.BUY/TradeEnum.SELL)
        """
        if trade_type == TradeEnum.BUY:
            return self._broker.buy_stock(code=code, buy_price=price, qty=qty)
        elif trade_type == TradeEnum.SELL:
            return self._broker.sell_stock(code=code, sell_price=price, qty=qty)
        else:
            raise ValueError(f"Trade type: {trade_type} not supported")

    # def modify_order(self, config: FTModifyOrderConfig):
    #     """
    #     修改订单
    #     TODO: 开发中
    #     不同的broker config 会有个别field不同

    #     参数:
    #     ibkr: IBKRModifyOrderConfig
    #     moomoo: FTModifyOrderConfig
    #     """
    #     return self._broker.modify_order(**config)

    def cancel_order(self, order_id: str) -> RetData:
        """取消订单"""
        return self._broker.cancel_order(order_id)

    def get_order_list(self, start_date: str = "", end_date: str = "") -> RetData:
        """
        获取账户下单列表
        参数
        start_date: 开始日期（YYYY-MM-DD）
        end_date: 结束日期（YYYY-MM-DD）
        """
        return self._broker.get_order_list(start_date=start_date, end_date=end_date)

    def get_position_list(self) -> pd.DataFrame:
        """获得当前仓位列表"""
        return self._broker.get_position_list()
