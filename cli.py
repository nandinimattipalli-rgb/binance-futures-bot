import argparse
import sys
from bot.validators import validate_inputs
from bot.orders import execute_futures_order

def main():
    parser = argparse.ArgumentParser(description="Primetrade.ai Production Testing Bot Framework")
    
    # Define positional arguments exactly matching the company checklist
    parser.add_argument("symbol", type=str, help="Trading pair (e.g., BTCUSDT)")
    parser.add_argument("side", type=str, help="Transaction side (BUY or SELL)")
    parser.add_argument("order_type", type=str, help="Execution structure (MARKET or LIMIT)")
    parser.add_argument("quantity", type=float, help="Asset lot size calculation amount")
    parser.add_argument("--price", "-p", type=float, default=None, help="Target entry price (Required for LIMIT)")

    args = parser.parse_args()

    # 1. Input Validation Phase
    try:
        validate_inputs(args.symbol, args.side, args.order_type, args.quantity, args.price)
    except ValueError as val_err:
        print(f"\n❌ Input Validation Error: {str(val_err)}")
        sys.exit(1)

    # 2. Print Request Summary
    print("\n--- [ Order Request Summary ] ---")
    print(f"Symbol:    {args.symbol.upper()}\nSide:      {args.side.upper()}\nType:      {args.order_type.upper()}\nQuantity:  {args.quantity}")
    if args.price: 
        print(f"Price:     ${args.price:,.2f}")
    print("---------------------------------")

    # 3. Execution Phase
    try:
        res = execute_futures_order(args.symbol, args.side, args.order_type, args.quantity, args.price)
        print("\n✅ ORDER PLACED SUCCESSFULLY")
        print(f"Order ID:      {res.get('orderId')}")
        print(f"Status:        {res.get('status')}")
        print(f"Executed Qty:  {res.get('executedQty')}")
        print(f"Avg Price:     {res.get('avgPrice', 'N/A')}")
    except Exception as api_err:
        print("\n❌ ORDER EXECUTION FAILED")
        print(f"Details: {str(api_err)}")

if __name__ == "__main__":
    main()