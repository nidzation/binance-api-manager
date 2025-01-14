import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv("config/.env")

# Get API keys
API_KEY = os.getenv("BINANCE_API_KEY")
SECRET_KEY = os.getenv("BINANCE_SECRET_KEY")

# Print keys
print(f"Loaded API Key: {API_KEY}")
print(f"Loaded Secret Key: {SECRET_KEY}")
