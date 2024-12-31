# File 3: trading_bot.py
# Main trading bot to execute the trading strategy.

import robin_stocks.robinhood as r
import pickle
import os
import time
import datetime
from strategyOriginal import execute_trade
from credentials import USERNAME, PASSWORD

SESSION_FILE = 'session.pickle'

def login():
    """
    Logs into Robinhood and saves authentication details for 24 hours.
    """
    if os.path.exists(SESSION_FILE):
        with open(SESSION_FILE, 'rb') as file:
            login_data = pickle.load(file)
        r.login(**login_data)
        print("Session restored from file.")
    else:
        mfa_code = input("Enter MFA code from authentication app: ")
        login_data = r.login(USERNAME, PASSWORD, mfa_code=mfa_code)
        with open(SESSION_FILE, 'wb') as file:
            pickle.dump(login_data, file)
        print("Logged in and session saved.")

def is_market_closed():
    """
    Check if the market is closed between Friday 8:00 PM and Sunday 8:00 PM EST.
    """
    now = datetime.datetime.now()
    # Determine the start and end time for the market closure window
    weekday = now.weekday()
    hour = now.hour
    
    if (weekday == 4 and hour >= 20) or (weekday == 5) or (weekday == 6 and hour < 20):
        return True
    return False

def check_cash_and_place_order(ticker, quantity=1):
    """
    Check if there is enough cash to place the buy order.
    Terminate if not enough cash is available.
    """
    try:
        # Fetch account cash balance
        account_info = r.profiles.load_account_profile()
        cash_available = float(account_info['cash'])
        print(f"Cash available: ${cash_available}")
        
        # Fetch real-time price
        last_price = float(r.stocks.get_latest_price(ticker, includeExtendedHours=False)[0])
        order_value = quantity * last_price
        print(f"Order value for {quantity} shares at ${last_price} per share: ${order_value}")
        
        if cash_available < order_value:
            print("Not enough cash to place the buy order. Terminating bot.")
            exit()
        
        print("Enough cash available. Proceeding with trade.")
        execute_trade(ticker)
        
    except Exception as e:
        print(f"Error checking cash or placing order: {e}")
        exit()

def main():
    """
    Main function to run the trading bot.
    """
    login()
    if is_market_closed():
        print("Stock Market is closed")
        return
    
    TICKER = 'TSLA'
    while True:
        try:
            check_cash_and_place_order(TICKER)
            time.sleep(60)  # Wait for 1 minute before checking again
        except KeyboardInterrupt:
            print("Bot stopped by user.")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            time.sleep(60)

if __name__ == '__main__':
    main()
