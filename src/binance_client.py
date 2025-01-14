import os
from dotenv import load_dotenv
from binance.client import Client

# Load environment variables
load_dotenv("config/.env")

# Get API keys
API_KEY = os.getenv("BINANCE_API_KEY")
SECRET_KEY = os.getenv("BINANCE_SECRET_KEY")

# Validate keys
if not API_KEY or not SECRET_KEY:
    raise Exception("API key and/or Secret key are missing.")

# Create Binance client
def get_binance_client():
    return Client(API_KEY, SECRET_KEY)
