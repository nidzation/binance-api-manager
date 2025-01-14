import logging
from binance_client import get_binance_client

# Configure logging
logging.basicConfig(
    filename="logs/account_summary.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def fetch_account_summary():
    try:
        print("Fetching account summary...")  # Debug output
        logging.info("Fetching account summary...")
        client = get_binance_client()
        account_info = client.get_account()
        balances = account_info.get("balances", [])

        for asset in balances:
            asset_name = asset["asset"]
            free_balance = float(asset["free"])
            locked_balance = float(asset["locked"])
            if free_balance > 0 or locked_balance > 0:
                logging.info(f"{asset_name}: Free = {free_balance}, Locked = {locked_balance}")
                print(f"{asset_name}: Free = {free_balance}, Locked = {locked_balance}")  # Debug output
    except Exception as e:
        logging.error(f"Failed to fetch account summary: {e}")
        print(f"Error: {e}")  # Debug output

if __name__ == "__main__":
    fetch_account_summary()
