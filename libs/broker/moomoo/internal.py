import moomoo as ft
from ..interface import BrokerStrategy
from ..constant import TradeEnvEnum, TradeMarketEnum


class MooMooBroker(BrokerStrategy):
    def __init__(
        self,
        host: str,
        port: int,
        trd_env: str = TradeEnvEnum.PAPER,
        trd_market: str = TradeMarketEnum.USStock,
        trd_firm=ft.SecurityFirm.FUTUSG,
    ) -> None:
        self.__trd_env = (
            ft.TrdEnv.REAL if trd_env == TradeEnvEnum.REAL else ft.TrdEnv.SIMULATE
        )

        self.__trd_ctx = ft.OpenSecTradeContext(
            host=host,
            port=port,
            filter_trdmarket=self.__get_trd_market(trd_market),
            is_encrypt=None,
            security_firm=trd_firm,
        )

    def get_account_info(self):
        return self.__trd_ctx.accinfo_query(
            trd_env=self.__trd_env,
            currency=ft.Currency.USD,
            refresh_cache=True,
        )

    def buy_stock(self, code, buy_price, qty):
        return self.__trd_ctx.place_order(
            price=buy_price,
            code=code,
            qty=qty,
            trd_side=ft.TrdSide.BUY,
            trd_env=self.__trd_env,
        )

    def sell_stock(
        self,
        code,
        sell_price,
        qty,
    ):

        return self.__trd_ctx.place_order(
            price=sell_price,
            code=code,
            qty=qty,
            trd_side=ft.TrdSide.SELL,
            trd_env=self.__trd_env,
        )

    def modify_order(self, order_id: str, qty: int, price: float):
        """开发中"""
        return self.__trd_ctx.modify_order(order_id, qty=qty, price=price)

    def get_order_list(
        self,
        start_date: str = "",
        end_date: str = "",
        order_status_list: list[str] = [
            ft.OrderStatus.SUBMITTING,
            ft.OrderStatus.SUBMITTED,
            ft.OrderStatus.FILLED_PART,
            ft.OrderStatus.FILLED_ALL,
        ],
    ):
        return self.__trd_ctx.order_list_query(
            start=start_date,
            end=end_date,
            status_filter_list=order_status_list,
            refresh_cache=True,
            trd_env=self.__trd_env,
        )

    def cancel_order(self, order_id: str):
        return self.__trd_ctx.modify_order(
            modify_order_op=ft.ModifyOrderOp.CANCEL,
            order_id=order_id,
            trd_env=self.__trd_env,
            qty=0,
            price=0,
        )

    def get_position_list(self):
        return self.__trd_ctx.position_list_query()

    def close(self):
        """关闭Broker 以防止没必要的链接数量浪费"""
        self.__trd_ctx.close()

    def __unlock_account(self):
        """真实交易环境前需要解锁账户"""
        self.__trd_ctx.unlock_trade(is_unlock=True)

    def __get_trd_market(self, trd_market: TradeMarketEnum):
        if trd_market == TradeMarketEnum.USStock:
            return ft.TrdMarket.US
        elif trd_market == TradeMarketEnum.HKStocks:
            return ft.TrdMarket.HK
        return None
