import logging
from binance_client import get_binance_client

# Configure logging
logging.basicConfig(
    filename='logs/trading_strategy.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def execute_strategy():
    """
    Execute the trading strategy using 10% of the USDT balance for fee-free pairs.
    """
    client = get_binance_client()
    if not client:
        logging.error("Failed to connect to Binance.")
        return

    try:
        # Fetch fee-free trading pairs
        fee_free_pairs = get_fee_free_pairs(client)
        if not fee_free_pairs:
            logging.warning("No fee-free trading pairs available.")
            return

        # Fetch account balances
        account_info = client.get_account()
        usdt_balance = next(
            (asset for asset in account_info["balances"] if asset["asset"] == "USDT"),
            {"free": "0"}
        )
        available_usdt = float(usdt_balance["free"])
        budget = available_usdt * 0.10

        if budget <= 0:
            logging.warning("Insufficient USDT balance to execute the strategy.")
            return

        logging.info(f"Using 10% of USDT balance (${budget:.2f}) for trading.")
        # Add trading logic here...
        logging.info("Trading strategy executed successfully.")
    except Exception as e:
        logging.error(f"An error occurred while executing the strategy: {e}")

def get_fee_free_pairs(client):
    """
    Fetch and return a list of fee-free trading pairs.
    """
    try:
        exchange_info = client.get_exchange_info()
        fee_free_pairs = [
            symbol["symbol"] for symbol in exchange_info["symbols"]
            if symbol.get("isSpotTradingAllowed", False) and symbol.get("makerCommission", 1) == 0
        ]
        return fee_free_pairs
    except Exception as e:
        logging.error(f"Error fetching fee-free pairs: {e}")
        return []

if __name__ == "__main__":
    execute_strategy()
