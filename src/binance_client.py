import os
import base64
import time
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives import serialization
from dotenv import load_dotenv

# Load environment variables
load_dotenv("config/.env")

API_KEY = os.getenv("BINANCE_API_KEY")
PRIVATE_KEY_STR = os.getenv("BINANCE_PRIVATE_KEY")

if not API_KEY or not PRIVATE_KEY_STR:
    raise Exception("API key or private key is missing.")

# Load private key
try:
    private_key = serialization.load_pem_private_key(
        PRIVATE_KEY_STR.encode(),
        password=None
    )
except Exception as e:
    raise RuntimeError(f"Failed to load private key: {e}")

def generate_ed25519_signature(http_method, endpoint, payload=""):
    """Generate ED25519 signature for Binance API requests."""
    timestamp = str(int(time.time() * 1000))
    message = f"{http_method}\n{endpoint}\n{timestamp}\n{payload}"
    signature = private_key.sign(message.encode())
    signature_b64 = base64.b64encode(signature).decode()

    return {
        "X-MBX-APIKEY": API_KEY,
        "X-MBX-SIGNATURE": signature_b64,
        "X-MBX-TIMESTAMP": timestamp,
    }
