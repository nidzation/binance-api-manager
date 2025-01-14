import logging
from binance_client import get_binance_client

# Constants
TEST_USDT_AMOUNT = 10.0  # Amount for test trades

# Setup logging
logging.basicConfig(
    filename="logs/trading_strategy.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def execute_trading_strategy():
    try:
        client = get_binance_client()

        # Check USDT balance
        account_info = client.get_account()
        usdt_balance = next(
            (balance for balance in account_info["balances"] if balance["asset"] == "USDT"), None
        )
        available_usdt = float(usdt_balance["free"]) if usdt_balance else 0.0

        logging.info(f"Available USDT: {available_usdt}")
        if available_usdt < TEST_USDT_AMOUNT:
            logging.warning("Insufficient USDT for test trade.")
            return

        # Fetch BTC price
        ticker = client.get_symbol_ticker(symbol="BTCUSDT")
        btc_price = float(ticker["price"])
        logging.info(f"Current BTC/USDT Price: {btc_price}")

        # Calculate BTC quantity
        btc_quantity = round(TEST_USDT_AMOUNT / btc_price, 6)
        logging.info(f"Calculated BTC Quantity for Test Trade: {btc_quantity}")

        # Place test order
        test_order = client.create_test_order(
            symbol="BTCUSDT",
            side="BUY",
            type="MARKET",
            quantity=btc_quantity,
        )
        logging.info(f"Test Order Successful: {test_order}")
    except Exception as e:
        logging.error(f"Error executing trading strategy: {e}")

if __name__ == "__main__":
    execute_trading_strategy()
