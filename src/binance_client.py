from binance.client import Client
from dotenv import load_dotenv
import os

load_dotenv()

def get_binance_client():
    """
    Initialize and return the Binance API client.
    """
    api_key = os.getenv("BINANCE_API_KEY")
    secret_key = os.getenv("BINANCE_SECRET_KEY")

    if not api_key or not secret_key:
        print("API key and/or Secret key are missing.")
        return None

    try:
        client = Client(api_key, secret_key)
        print("Binance client successfully initialized.")
        return client
    except Exception as e:
        print(f"Failed to initialize Binance client: {e}")
        return None
