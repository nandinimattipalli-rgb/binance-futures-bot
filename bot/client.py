import os
from dotenv import load_dotenv
from binance.um_futures import UMFutures

load_dotenv()

def get_binance_client():
    api_key = os.getenv("BINANCE_TESTNET_API_KEY", "").strip()
    api_secret = os.getenv("BINANCE_TESTNET_API_SECRET", "").strip()
    
    if not api_key or not api_secret:
        raise RuntimeError("Missing API keys in your .env configuration file.")
        
    return UMFutures(
        key=api_key, 
        secret=api_secret, 
        base_url="https://testnet.binancefuture.com"
    )