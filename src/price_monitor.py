import time
from binance_client import get_binance_client

# Constants for the symbol to monitor
SYMBOL = "BTCUSDT"
INTERVAL = 5  # Interval in seconds for price updates

def get_price(client, symbol):
    try:
        ticker = client.get_symbol_ticker(symbol=symbol)
        return float(ticker["price"])
    except Exception as e:
        print(f"Error fetching price for {symbol}: {e}")
        return None

def monitor_price():
    client = get_binance_client()
    if not client:
        print("Failed to initialize Binance client. Exiting.")
        return

    print(f"Starting price monitoring for {SYMBOL}...")
    try:
        while True:
            price = get_price(client, SYMBOL)
            if price:
                print(f"Current price of {SYMBOL}: {price}")
            time.sleep(INTERVAL)
    except KeyboardInterrupt:
        print("\nPrice monitoring stopped.")

if __name__ == "__main__":
    monitor_price()
