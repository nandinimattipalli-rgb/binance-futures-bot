def validate_inputs(symbol: str, side: str, order_type: str, quantity: float, price: float = None):
    errors = []
    if not symbol.endswith("USDT"):
        errors.append("Symbol must be a USDT pair (e.g., BTCUSDT).")
    if side.upper() not in ["BUY", "SELL"]:
        errors.append("Side must be either BUY or SELL.")
    if order_type.upper() not in ["MARKET", "LIMIT"]:
        errors.append("Order type must be either MARKET or LIMIT.")
    if quantity <= 0:
        errors.append("Quantity must be greater than zero.")
    if order_type.upper() == "LIMIT" and (price is None or price <= 0):
        errors.append("Price is strictly required and must be greater than zero for LIMIT orders.")
    
    if errors:
        raise ValueError(" | ".join(errors))