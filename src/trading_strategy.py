from binance_client import get_binance_client
import logging

# Initialize logging
logging.basicConfig(
    filename="asset_allocation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def check_assets():
    client = get_binance_client()
    if not client:
        print("Failed to initialize Binance client. Exiting.")
        return

    print("Fetching asset allocation...")
    try:
        account_info = client.get_account()
        balances = account_info.get("balances", [])
        
        # Filter assets with non-zero balances
        non_zero_assets = [asset for asset in balances if float(asset["free"]) > 0 or float(asset["locked"]) > 0]

        if non_zero_assets:
            print("\nYour asset allocation:")
            logging.info("Asset Allocation:")
            for asset in non_zero_assets:
                free = float(asset["free"])
                locked = float(asset["locked"])
                print(f"- {asset['asset']}: Free = {free}, Locked = {locked}")
                logging.info(f"{asset['asset']}: Free = {free}, Locked = {locked}")
        else:
            print("No assets found in your account.")
            logging.info("No assets found in the account.")
    except Exception as e:
        logging.error(f"Error fetching assets: {e}")
        print(f"Error fetching assets: {e}")

if __name__ == "__main__":
    check_assets()
