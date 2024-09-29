import pytest
from broker import MooMooBroker
from .moomoo_ctx import get_broker
import moomoo as ft

@pytest.fixture()
def broker()->MooMooBroker:
    return get_broker()

# def test_moomoo_buy_stock(broker)->None:
#     code, order_data = broker.buy_stock(code="US.SOUN", buy_price=2, qty=20)
#     assert code == ft.RET_OK
#     code, order_data_list = broker.get_order_list()
#     assert  order_data["order_id"].isin(order_data_list["order_id"].values).bool()



