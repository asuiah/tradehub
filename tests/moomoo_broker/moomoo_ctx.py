from broker import MooMooBroker
from broker.constant import TradeEnvEnum


def get_broker()->MooMooBroker:
    return MooMooBroker(
        host="127.0.0.1",
        port=6066,
        trd_env=TradeEnvEnum.PAPER,
    )
