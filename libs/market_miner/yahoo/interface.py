from typing import TypedDict, Literal
from enum import Enum


class Period(Enum):
    YSTERDAY = "ytd"
    ONE_DAY = "1d"
    FIVE_DAYS = "5d"
    ONE_MONTH = "1mo"
    THREE_MONTHS = "3mo"
    SIX_MONTHS = "6mo"
    ONE_YEAR = "1y"
    TWO_YEARS = "2y"
    FIVE_YEARS = "5y"
    TEN_YEARS = "10y"
    MAX = "max"


class Interval(Enum):
    ONE_MIN = "1m"
    TWO_MINS = "2m"
    FIVE_MINS = "5m"
    FIFTEN_MINS = "15m"
    THIRDY_MINS = "30m"
    SIXTY_MINS = "60m"
    NIGHTY_MINS = "90m"
    ONE_HOUR = "1h"
    ONE_DAY = "1d"
    FIVE_DAYS = "5d"
    ONE_WEEK = "1wk"
    ONE_MONTH = "1mo"
    THREE_MONTHS = "1mo"


class YahooAPIConfig(TypedDict):
    start: str
    end: str
    tickers: list[str]
    period: Literal[
        "1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max"
    ]
    interval: Literal[
        "1m",
        "2m",
        "5m",
        "15m",
        "30m",
        "60m",
        "90m",
        "1h",
        "1d",
        "5d",
        "1wk",
        "1mo",
        "3mo",
    ]
    prepost: bool
