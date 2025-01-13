import os
from binance.client import Client
from dotenv import load_dotenv

def main():
    # Load environment variables
    load_dotenv(dotenv_path="config/.env")
    
    api_key = os.getenv("BINANCE_API_KEY")
    secret_key = os.getenv("BINANCE_SECRET_KEY")

    # Initialize Binance client
    client = Client(api_key, secret_key)
    
    # Fetch account information
    try:
        account_info = client.get_account()
        balances = account_info['balances']
        
        print("Your Assets and Allocations:")
        for balance in balances:
            asset = balance['asset']
            free = float(balance['free'])
            locked = float(balance['locked'])
            total = free + locked
            if total > 0:  # Show only assets with non-zero balance
                print(f"{asset}: Free = {free}, Locked = {locked}, Total = {total}")
    except Exception as e:
        print(f"Error fetching account information: {e}")

if __name__ == "__main__":
    main()
