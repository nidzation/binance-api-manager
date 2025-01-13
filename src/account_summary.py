from binance_client import get_binance_client

def fetch_account_summary():
    """
    Fetch and display the user's account asset allocation.
    """
    client = get_binance_client()
    if not client:
        print("Failed to connect to Binance. Please check your API credentials.")
        return

    try:
        print("Fetching account summary...")
        account_info = client.get_account()
        balances = account_info.get("balances", [])
        
        # Filter for assets with non-zero balances
        assets = [asset for asset in balances if float(asset["free"]) > 0 or float(asset["locked"]) > 0]

        if assets:
            print("\nYour Account Summary:")
            print("-" * 30)
            for asset in assets:
                free = float(asset["free"])
                locked = float(asset["locked"])
                print(f"{asset['asset']}:")
                print(f"  Free: {free}")
                print(f"  Locked: {locked}")
            print("-" * 30)
        else:
            print("No assets found in your account.")
    except Exception as e:
        print(f"An error occurred while fetching the account summary: {e}")

if __name__ == "__main__":
    fetch_account_summary()
