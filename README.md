# tradehub

## Developer Documentation

### Install vscode extension

- Flake8
- Black Formatter

### Setup environment

#### 1.Create virtual env

Project using poetry for package management. poetry install package in .venv folder if exist. otherwise install in the poetry cache directory (check cache-dir by using ***poetry config --list*** )

```bash
    python -m venv .venv
```

#### 2.Install poetry

```bash
    pip install poetry
```

#### 3.Install package via poetry

```bash
    poetry install
```

#### 4.Setup pre-commit tool for the first time

```bash
    pre-commit install
    pre-commit install --hook-type commit-msg
```

#### 5.Ensure use Poetry to install package

Poetry auto update a lock file for each installation to ensure the package version security.

```bash
poetry add <package>
poetry remove <package>
```

## Project modules

### market_miner

Fetching market data from multiple provider. Now only support for Yahoo finance (yFinance)

- Yahoo
- CNBC

example:

```python
from alpha.market_miner.yahoo.interface import YahooAPIConfig
from alpha.market_miner.singleton import MarketMiner
from alpha.market_miner.transformer.transform_yfinance_df import TransformYFinanceDF

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

    # Transform data per biz requirement
    pandasTransformer = TransformYFinanceDF()
    postData = fetcher.process_data(pandasTransformer, data)
    print("postedData \n", postData)

```

### Broker

- MooMoo (prerequesit: install [OpenD](https://www.moomoo.com/download/OpenAPI) openD is a gateway for moomoo transactions)
- IBKR (Developing)

example

```python

from alpha.broker.moomoo.internal import MooMooBroker
from alpha.broker.constant import TradeEnum, TradeEnvEnum
from alpha.broker.broker_ctx import BrokerCtx

if __name__ == "__main__":
    moomoo_broker = MooMooBroker(
        host="127.0.0.1",
        port=6066,
        trd_env=TradeEnvEnum.PAPER,
    )
    broker_ctx = BrokerCtx(moomoo_broker)
    # Buy stock
    code, order_data = broker_ctx.trade(
        code="US.SOUN", price=3, qty=10, trade_type=TradeEnum.BUY
    )
    print(code, order_data)
    # Cancel stock
    code, data = broker_ctx.cancel_order(order_id=order_data.iloc[0]["order_id"])
    print(code, order_data)

    # Sell stock
    code, data = broker_ctx.trade(
        code="US.SOUN", price=3, qty=10, trade_type=TradeEnum.SELL
    )
    print(code, order_data)

    # Get order list
    code, data = broker_ctx.get_order_list()
    print(code, data)

    # Get position list
    code, data = broker_ctx.get_position_list()
    print(code, data)


```

### tests

Run tests

```python
python -m unittest discover -s tests
```
