from decimal import Decimal
from binance.exceptions import BinanceAPIException

def get_top_coins(client, limit=10):
    tickers = client.get_ticker()
    sorted_tickers = sorted(tickers, key=lambda x: float(x['quoteVolume']), reverse=True)
    return [ticker['symbol'] for ticker in sorted_tickers if ticker['symbol'].endswith('USDT')][:limit]

def get_trade_filters(client, symbol):
    exchange_info = client.get_exchange_info()
    for s in exchange_info['symbols']:
        if s['symbol'] == symbol:
            filters = {f['filterType']: f for f in s['filters']}
            return {
                "minQty": Decimal(filters['LOT_SIZE']['minQty']),
                "stepSize": Decimal(filters['LOT_SIZE']['stepSize']),
                "minNotional": Decimal(filters['MIN_NOTIONAL']['minNotional']),
            }
    raise ValueError(f"Filters not found for {symbol}.")

def place_order(client, symbol, usdt_amount, real_trade=False):
    try:
        if real_trade:
            order = client.create_order(
                symbol=symbol,
                side="BUY",
                type="MARKET",
                quoteOrderQty=float(usdt_amount),
            )
            return order
        else:
            return f"Simulated order: Buy {usdt_amount} USDT worth of {symbol}"
    except BinanceAPIException as e:
        raise RuntimeError(f"Order failed for {symbol}: {e}")
