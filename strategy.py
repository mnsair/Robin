# File 2: strategy.py
# Trading strategy using live data from Robinhood.

import robin_stocks.robinhood as r
import pandas as pd
import yfinance as yf
import time
import sys

def check_trading_conditions(ticker):
    """
    Check if the trading conditions are met for buying.
    Conditions:
    1. 9EMA is above VWAP on a 5-minute chart.
    2. 9EMA crosses above 50SMA on a 1-minute chart.
    """
    # Fetch live data
    data_1min = yf.download(tickers=ticker, period='1d', interval='1m')
    data_5min = yf.download(tickers=ticker, period='1d', interval='5m')
    
    if data_1min.empty or data_5min.empty:
        print("Failed to fetch data from Yahoo Finance.")
        return False
    
    # Calculate indicators
    data_5min['9EMA'] = data_5min['Close'].ewm(span=9).mean()
    data_5min['VWAP'] = (data_5min['Close'] * data_5min['Volume']).cumsum() / data_5min['Volume'].cumsum()
    
    data_1min['9EMA'] = data_1min['Close'].ewm(span=9).mean()
    data_1min['50SMA'] = data_1min['Close'].rolling(window=50).mean()
    
    # Check conditions
    condition1 = data_5min['9EMA'].iloc[-1] > data_5min['VWAP'].iloc[-1]
    condition2 = data_1min['9EMA'].iloc[-2] <= data_1min['50SMA'].iloc[-2] and data_1min['9EMA'].iloc[-1] > data_1min['50SMA'].iloc[-1]
    
    return condition1 and condition2

def monitor_order(order_id, timeout=300):
    """
    Monitor an order until it is filled or timeout is reached.
    """
    start_time = time.time()
    while time.time() - start_time < timeout:
        order_status = r.orders.get_stock_order_info(order_id)
        if order_status['state'] == 'filled':
            print("Buy order executed successfully.")
            return True
        print("Waiting for buy order to fill...")
        time.sleep(10)
    print("Timeout reached while waiting for buy order to fill.")
    return False

def execute_trade(ticker):
    """Execute the buy and sell orders based on conditions."""
    if check_trading_conditions(ticker):
        bid_price = float(r.stocks.get_latest_price(ticker, includeExtendedHours=False)[0])
        # Place a buy limit order
        buy_order = r.orders.order_buy_limit(ticker, quantity=1, limitPrice=bid_price)
        print(f"Buy Order Placed at ${bid_price}: {buy_order}")
        
        if buy_order and monitor_order(buy_order['id']):
            sell_price = bid_price + 1.51
            # Place a sell limit order
            sell_order = r.orders.order_sell_limit(ticker, quantity=1, limitPrice=sell_price)
            print(f"Sell Order Placed for 1 share at ${sell_price}")
            print("Sell Order Placed for 1 at ${sell_price}. Terminating bot.")
            sys.exit()
        else:
            print("Buy order not filled. Skipping sell order.")
    else:
        print("Conditions not met for trading.")

if __name__ == '__main__':
    TICKER = 'TSLA'
    execute_trade(TICKER)
