
import os

BITFINEX_API_KEY = os.environ.get("BITFINEX_API_KEY")
BITFINEX_API_SECRET = os.environ.get("BITFINEX_API_SECRET")

TRADE_AMOUNT_USD = 5
SYMBOLS = ["LTCUSD", "BTCUSD", "ETHUSD", "XRPUSD"]
BASE_URL = "https://api.bitfinex.com"
