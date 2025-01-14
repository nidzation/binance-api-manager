import logging
from binance_client import get_binance_client

# Configure logging
logging.basicConfig(
    filename='logs/account_summary.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def fetch_account_summary():
    """
    Fetch and display the user's complete account asset allocation.
    """
    client = get_binance_client()
    if not client:
        logging.error("Failed to connect to Binance. Please check your API credentials.")
        return

    try:
        logging.info("Fetching complete account assets...")
        account_info = client.get_account()
        balances = account_info.get("balances", [])

        # Filter and log assets with non-zero balances
        assets = [asset for asset in balances if float(asset["free"]) > 0 or float(asset["locked"]) > 0]
        for asset in assets:
            logging.info(f"{asset['asset']}: Free = {asset['free']}, Locked = {asset['locked']}")
        print("Account summary logged successfully.")
    except Exception as e:
        logging.error(f"An error occurred while fetching account assets: {e}")
        print("Failed to fetch account summary. Check logs for details.")

if __name__ == "__main__":
    fetch_account_summary()
