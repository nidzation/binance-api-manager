from binance.client import Client
import os
from dotenv import load_dotenv

load_dotenv('config/.env')

api_key = os.getenv('BINANCE_API_KEY')
api_secret = os.getenv('BINANCE_SECRET_KEY')

if not api_key or not api_secret:
    print("API key and/or secret key are missing.")
else:
    try:
        client = Client(api_key, api_secret)
        account_info = client.get_account()
        print("Connection successful! Account data retrieved:")
        print(account_info)
    except Exception as e:
        print(f"Error connecting to Binance: {e}")
