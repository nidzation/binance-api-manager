import logging
from binance_client import get_binance_client

# Setup logging
logging.basicConfig(
    filename="logs/test_binance_connection.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def test_binance_connection():
    try:
        client = get_binance_client()
        status = client.get_system_status()
        logging.info(f"Binance API Status: {status['msg']} (Code: {status['status']})")
        print(f"Binance API Status: {status['msg']} (Code: {status['status']})")
    except Exception as e:
        logging.error(f"Error connecting to Binance API: {e}")
        print(f"Error connecting to Binance API: {e}")

if __name__ == "__main__":
    test_binance_connection()
