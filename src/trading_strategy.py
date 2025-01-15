import os
import logging
from decimal import Decimal
from dotenv import load_dotenv
from binance.client import Client
from binance.exceptions import BinanceAPIException

# Load environment variables
load_dotenv("config/.env")

# Set up API keys
API_KEY = os.getenv("BINANCE_API_KEY")
SECRET_KEY = os.getenv("BINANCE_SECRET_KEY")

# Set up logging
logging.basicConfig(
    filename="logs/trading_strategy.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Validate keys
if not API_KEY or not SECRET_KEY:
    raise Exception("API key and/or Secret key are missing.")

# Initialize Binance client
client = Client(API_KEY, SECRET_KEY)

# Constants
USDT_PER_COIN = Decimal("1.0")  # Amount of USDT to trade per coin
REAL_TRADE = False  # Toggle real trades on/off

def get_top_10_coins():
    """Fetch the top 10 coins by 24-hour trading volume."""
    tickers = client.get_ticker()
    sorted_tickers = sorted(tickers, key=lambda x: float(x['quoteVolume']), reverse=True)
    return [ticker['symbol'] for ticker in sorted_tickers if ticker['symbol'].endswith('USDT')][:10]

def get_minimum_trade_amount(symbol):
    """Get the minimum trade amount (notional) for a given symbol."""
    exchange_info = client.get_exchange_info()
    for s in exchange_info['symbols']:
        if s['symbol'] == symbol:
            for f in s['filters']:
                if f['filterType'] == 'MIN_NOTIONAL':
                    return Decimal(f['minNotional'])
    raise ValueError(f"Symbol {symbol} does not have a MIN_NOTIONAL filter.")

def place_market_order(symbol, usdt_amount):
    """Place a market order using a specific USDT amount."""
    try:
        if REAL_TRADE:
            order = client.create_order(
                symbol=symbol,
                side="BUY",
                type="MARKET",
                quoteOrderQty=float(usdt_amount),
            )
            logging.info(f"Market order placed for {symbol}: {order}")
            return order
        else:
            logging.info(f"Simulated order: Buy {usdt_amount} USDT worth of {symbol}")
            print(f"Simulated order: Buy {usdt_amount} USDT worth of {symbol}")
            return None
    except BinanceAPIException as e:
        logging.error(f"Order failed for {symbol}: {e}")
        print(f"Order failed for {symbol}: {e}")
        return None

def main():
    try:
        # Fetch account balance
        logging.info("Executing trading strategy...")
        account_info = client.get_account()
        balances = {balance['asset']: Decimal(balance['free']) for balance in account_info['balances']}
        usdt_balance = balances.get('USDT', Decimal(0))

        print(f"Available USDT balance: {usdt_balance}")
        logging.info(f"Available USDT balance: {usdt_balance}")

        if usdt_balance < USDT_PER_COIN * 10:
            logging.warning("Insufficient USDT for trading.")
            print("Insufficient USDT for trading.")
            return

        # Fetch top 10 coins by trading volume
        top_10_coins = get_top_10_coins()
        print(f"Top 10 coins: {top_10_coins}")
        logging.info(f"Top 10 coins: {top_10_coins}")

        for symbol in top_10_coins:
            try:
                # Get minimum trade amount for the symbol
                min_trade_amount = get_minimum_trade_amount(symbol)
                usdt_to_trade = max(USDT_PER_COIN, min_trade_amount)

                if usdt_to_trade > usdt_balance:
                    logging.warning(f"Not enough USDT for {symbol}. Needed: {usdt_to_trade}")
                    print(f"Not enough USDT for {symbol}. Needed: {usdt_to_trade}")
                    continue

                # Execute the trade
                place_market_order(symbol, usdt_to_trade)

            except Exception as e:
                logging.error(f"Unexpected error for {symbol}: {e}")
                print(f"Unexpected error for {symbol}: {e}")

    except BinanceAPIException as e:
        logging.error(f"API error: {e}")
        print(f"Error: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
