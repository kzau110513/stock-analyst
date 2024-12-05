import yfinance as yf

# Get real-time data for a stock
ticker = yf.Ticker("AAPL")
data = ticker.history(period="1d", interval="1m")
print(data.tail())
