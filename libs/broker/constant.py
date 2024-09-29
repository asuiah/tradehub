class TradeEnum:
    SELL = "SELL"
    BUY = "BUY"


class OrderEnum:
    STOCK = "STOCK"
    OPTION = "OPTION"


class TradeEnvEnum:
    PAPER = "PAPER_TRADING"
    REAL = "REAL"


class TradeMarketEnum:
    USStock = "US_STOCK"
    HKStocks = "HK_STOCK"


class HttpErrorCode:
    SUCCESS = 200
    BAD_REQUEST = 400
    FORBIDDEN = 403
    INTERNAL_ERROR = 500
