import logging
import requests
from decimal import Decimal
from dotenv import load_dotenv
import os
from binance_client import sign_request

# Load environment variables
load_dotenv("config/.env")

# Constants
BASE_URL = "https://api.binance.com"
USDT_ALLOCATION = Decimal("20")  # Total USDT allocated for trades
MAX_COINS = 10  # Limit for the number of coins to trade

# Set up logging
logging.basicConfig(
    filename="logs/trading_strategy.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def fetch_profitable_coins():
    """Fetch top profitable coins."""
    endpoint = "/api/v3/ticker/24hr"
    try:
        response = requests.get(f"{BASE_URL}{endpoint}")
        response.raise_for_status()
        tickers = response.json()
        profitable_coins = [
            {
                "symbol": ticker["symbol"],
                "priceChangePercent": Decimal(ticker["priceChangePercent"]),
            }
            for ticker in tickers
            if ticker["symbol"].endswith("USDT") and Decimal(ticker["priceChangePercent"]) > 0
        ]
        profitable_coins.sort(key=lambda x: x["priceChangePercent"], reverse=True)
        return profitable_coins[:MAX_COINS]
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to fetch profitable coins: {e}")
        raise RuntimeError("Failed to fetch profitable coins.") from e


def execute_conversions(coins):
    """Execute conversions using the Convert endpoint."""
    for coin in coins:
        base_asset = coin["symbol"][:-4]
        endpoint = "/sapi/v1/convert/trade"
        payload = f"fromAsset=USDT&toAsset={base_asset}&amount={USDT_ALLOCATION / MAX_COINS}"
        headers = sign_request("POST", endpoint, payload)

        try:
            response = requests.post(f"{BASE_URL}{endpoint}", headers=headers, data=payload)
            logging.info(f"Request: {payload}")
            logging.info(f"Response: {response.status_code} {response.text}")
            response.raise_for_status()
            print(f"Converted {USDT_ALLOCATION / MAX_COINS} USDT to {base_asset}.")
        except requests.exceptions.RequestException as e:
            logging.warning(f"Conversion failed for {base_asset}: {response.text} ({e})")
            print(f"Conversion failed for {base_asset}: {response.text} ({e})")


def main():
    logging.info("Fetching profitable coins...")
    try:
        profitable_coins = fetch_profitable_coins()
        logging.info("Top profitable coins fetched.")
        execute_conversions(profitable_coins)
    except Exception as e:
        logging.error(f"Error in main execution: {e}")
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
