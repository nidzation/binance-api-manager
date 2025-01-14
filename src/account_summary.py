import logging
from binance_client import get_binance_client

# Setup logging
logging.basicConfig(
    filename="logs/account_summary.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def fetch_account_summary():
    try:
        client = get_binance_client()
        account_info = client.get_account()
        logging.info("Fetching complete account assets...")

        for balance in account_info['balances']:
            asset = balance['asset']
            free = balance['free']
            locked = balance['locked']
            logging.info(f"{asset}: Free = {free}, Locked = {locked}")
    except Exception as e:
        logging.error(f"Error fetching account summary: {e}")

if __name__ == "__main__":
    fetch_account_summary()
