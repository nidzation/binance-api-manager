from binance_client import generate_ed25519_signature

# Test connection
try:
    headers = generate_ed25519_signature("GET", "/api/v3/time")
    print("Generated headers:", headers)
except Exception as e:
    print(f"Error: {e}")
