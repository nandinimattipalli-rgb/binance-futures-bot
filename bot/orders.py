from bot.client import get_binance_client
from bot.logging_config import setup_logging

logger = setup_logging()

def execute_futures_order(symbol: str, side: str, order_type: str, quantity: float, price: float = None):
    client = get_binance_client()
    
    params = {
        "symbol": symbol.upper(),
        "side": side.upper(),
        "type": order_type.upper(),
        "quantity": quantity
    }
    
    if order_type.upper() == "LIMIT":
        params["price"] = str(price)
        params["timeInForce"] = "GTC"

    logger.info(f"Sending Order Request Payload: {params}")
    
    try:
        response = client.new_order(**params)
        logger.info(f"Received Order Response: {response}")
        return response
    except Exception as e:
        logger.error(f"Binance Server Rejection Exception: {str(e)}")
        raise e