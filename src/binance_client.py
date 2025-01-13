import os
from binance.client import Client
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(dotenv_path="config/.env")

# Retrieve API credentials from the environment
API_KEY = os.getenv("BINANCE_API_KEY")
SECRET_KEY = os.getenv("BINANCE_SECRET_KEY")

# Initialize the Binance client
def get_binance_client():
    try:
        client = Client(API_KEY, SECRET_KEY)
        # Test the connection to Binance API
        client.ping()
        print("Binance client successfully initialized.")
        return client
    except Exception as e:
        print(f"Error initializing Binance client: {e}")
        return None

if __name__ == "__main__":
    client = get_binance_client()
    if client:
        # Example: Print account status
        account = client.get_account()
        print("Account information:", account)
