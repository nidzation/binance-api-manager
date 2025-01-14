from binance_client import get_binance_client

# Test connection to Binance API
try:
    client = get_binance_client()
    status = client.get_system_status()
    print(f"Binance API Status: {status['msg']} (Code: {status['status']})")
except Exception as e:
    print(f"Failed to connect to Binance API: {e}")
