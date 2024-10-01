import yfinance as yf

# Initialize an empty portfolio dictionary
portfolio = {}

# Static conversion rate from USD to INR (update this value as needed)
USD_TO_INR = 83.00

# Function to add a stock to the portfolio
def add_stock(symbol, shares, purchase_price):
    portfolio[symbol] = (shares, purchase_price)
    print(f"Added {symbol} with {shares} shares at ₹{purchase_price:.2f}")

# Function to remove a stock from the portfolio
def remove_stock(symbol):
    if symbol in portfolio:
        del portfolio[symbol]
        print(f"Removed {symbol} from portfolio")
    else:
        print(f"{symbol} not found in portfolio")

# Function to get real-time stock price using yfinance
def get_real_time_price(symbol):
    stock = yf.Ticker(symbol)
    try:
        print(f"Fetching data for {symbol}...")  # Debugging output
        current_price = stock.history(period='1d')['Close'].iloc[0]
        return current_price
    except (IndexError, ValueError) as e:
        print(f"Error fetching data for {symbol}: {str(e)}. Symbol may be delisted or invalid.")
        return None

# Function to track and display portfolio details in INR
def track_portfolio():
    total_value = 0
    print("\nPortfolio Summary:")
    for symbol, (shares, purchase_price) in portfolio.items():
        current_price = get_real_time_price(symbol)
        if current_price is None:
            print(f"Skipping {symbol} due to data fetch error.")
            continue
        
        # Convert current price and values to INR
        current_price_inr = current_price * USD_TO_INR
        purchase_price_inr = purchase_price * USD_TO_INR
        current_value_inr = shares * current_price_inr
        
        print(f"{symbol}: {shares} shares | Purchase Price: ₹{purchase_price_inr:.2f} | Current Price: ₹{current_price_inr:.2f} | Value: ₹{current_value_inr:.2f}")
        total_value += current_value_inr
    
    print(f"\nTotal Portfolio Value: ₹{total_value:.2f}\n")

# Main interactive loop for user input
def main():
    while True:
        print("\nStock Portfolio Tracker")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Track Portfolio")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            symbol = input("Enter stock symbol (e.g., AAPL): ").strip().upper()  # Convert to uppercase
            shares = int(input("Enter number of shares: "))
            purchase_price = float(input("Enter purchase price in USD: "))
            add_stock(symbol, shares, purchase_price)
        
        elif choice == '2':
            symbol = input("Enter stock symbol to remove: ").strip().upper()  # Convert to uppercase
            remove_stock(symbol)
        
        elif choice == '3':
            track_portfolio()
        
        elif choice == '4':
            print("Exiting the tracker.")
            break
        
        else:
            print("Invalid choice. Please try again.")

# Example usage
if __name__ == "__main__":
    main()
