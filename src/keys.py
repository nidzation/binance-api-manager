import os
from dotenv import load_dotenv

def load_api_keys(env_file="config/.env"):
    load_dotenv(env_file)
    api_key = os.getenv("BINANCE_API_KEY")
    secret_key = os.getenv("BINANCE_SECRET_KEY")

    if not api_key or not secret_key:
        raise ValueError("API key and/or Secret key are missing.")
    
    return api_key, secret_key
