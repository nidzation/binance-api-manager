from binance.client import Client
from config.keys import load_api_keys
from src.utils import setup_logging
from src.trade_helpers import get_top_coins, get_trade_filters, place_order
from decimal import Decimal

def main():
    # Initialize
    setup_logging("logs/trading_strategy.log")
    api_key, secret_key = load_api_keys()
    client = Client(api_key, secret_key)

    # Constants
    USDT_PER_COIN = Decimal("1.0")
    REAL_TRADE = False

    # Fetch account balance
    account_info = client.get_account()
    balances = {balance['asset']: Decimal(balance['free']) for balance in account_info['balances']}
    usdt_balance = balances.get('USDT', Decimal(0))

    if usdt_balance < USDT_PER_COIN * 10:
        print("Insufficient USDT for trading.")
        return

    # Fetch top coins
    top_coins = get_top_coins(client)
    for symbol in top_coins:
        try:
            filters = get_trade_filters(client, symbol)
            if USDT_PER_COIN < filters['minNotional']:
                print(f"Skipping {symbol}: USDT allocation {USDT_PER_COIN} below minNotional {filters['minNotional']}.")
                continue

            result = place_order(client, symbol, USDT_PER_COIN, REAL_TRADE)
            print(f"Order result for {symbol}: {result}")
        except Exception as e:
            print(f"Error for {symbol}: {e}")

if __name__ == "__main__":
    main()
