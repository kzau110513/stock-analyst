import yfinance as yf

# Fetch historical data for Apple (AAPL)
ticker = yf.Ticker("AAPL")
data = ticker.history(period="1mo", interval="1d")  # Last 1 month, daily intervals
print(data.head())  # Check the data format


import matplotlib.pyplot as plt

# Extract date and closing price
data['Date'] = data.index  # Convert index to a column for easier access
plt.figure(figsize=(10, 6))
plt.plot(data['Date'], data['Close'], label="Closing Price", color="blue")

# Customize the chart
plt.title("AAPL Stock Price (Last Month)", fontsize=16)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Closing Price (USD)", fontsize=12)
plt.legend()
plt.grid()
plt.xticks(rotation=45)
plt.tight_layout()

# Show the plot
plt.show()
