import os
import logging
from decimal import Decimal, ROUND_DOWN
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
TEST_USDT_AMOUNT = 10  # Use 10 USDT for testing
SYMBOL = "BTCUSDT"
REAL_TRADE = True  # Set to True to enable real trades


def get_minimum_order_info(symbol):
    """Fetch minimum quantity and step size for the given symbol."""
    exchange_info = client.get_exchange_info()
    for s in exchange_info['symbols']:
        if s['symbol'] == symbol:
            for f in s['filters']:
                if f['filterType'] == 'LOT_SIZE':
                    return Decimal(f['minQty']), Decimal(f['stepSize'])
    raise ValueError(f"Symbol {symbol} not found or missing LOT_SIZE filter.")


def adjust_quantity(quantity, step_size):
    """Adjust quantity to match step size."""
    return (quantity // step_size) * step_size


def main():
    try:
        # Fetch account balance
        logging.info("Executing trading strategy...")
        account_info = client.get_account()
        balances = {balance['asset']: Decimal(balance['free']) for balance in account_info['balances']}
        usdt_balance = balances.get('USDT', Decimal(0))

        print(f"Available USDT balance: {usdt_balance}")
        logging.info(f"Available USDT balance: {usdt_balance}")

        if usdt_balance < Decimal(TEST_USDT_AMOUNT):
            logging.warning("Insufficient USDT balance for the trade.")
            print("Insufficient USDT balance for the trade.")
            return

        # Get current BTC price
        ticker = client.get_symbol_ticker(symbol=SYMBOL)
        btc_price = Decimal(ticker['price'])
        print(f"Current BTC price: {btc_price}")
        logging.info(f"Current BTC price: {btc_price}")

        # Calculate BTC quantity
        min_qty, step_size = get_minimum_order_info(SYMBOL)
        btc_quantity = Decimal(TEST_USDT_AMOUNT) / btc_price
        btc_quantity = adjust_quantity(btc_quantity, step_size)

        print(f"Minimum BTC quantity: {min_qty}, Step size: {step_size}")
        print(f"Adjusted BTC quantity: {btc_quantity}")
        logging.info(f"Adjusted BTC quantity: {btc_quantity}")

        if btc_quantity < min_qty:
            logging.error(f"BTC quantity {btc_quantity} is below minimum order size {min_qty}.")
            print(f"BTC quantity {btc_quantity} is below minimum order size {min_qty}.")
            return

        # Place order
        if REAL_TRADE:
            order = client.create_order(
                symbol=SYMBOL,
                side="BUY",
                type="MARKET",
                quantity=float(btc_quantity),
            )
            print(f"Live order result: {order}")
            logging.info(f"Live order result: {order}")
        else:
            order = client.create_test_order(
                symbol=SYMBOL,
                side="BUY",
                type="MARKET",
                quantity=float(btc_quantity),
            )
            print(f"Test order result: {order}")
            logging.info(f"Test order result: {order}")

    except BinanceAPIException as e:
        logging.error(f"API error: {e}")
        print(f"Error: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
