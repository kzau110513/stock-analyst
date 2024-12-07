import yfinance as yf

# Define the ticker symbol
ticker = "AAPL"

# Get data for the ticker
stock_data = yf.Ticker(ticker)

# Fetch historical market data
hist = stock_data.history(period="1mo")

# Display the historical data
print(hist)

import matplotlib.pyplot as plt

# Calculate moving averages
hist['MA20'] = hist['Close'].rolling(window=20).mean()
hist['MA50'] = hist['Close'].rolling(window=50).mean()

# Plot the data
plt.figure(figsize=(10, 5))
plt.plot(hist['Close'], label='Close Price')
plt.plot(hist['MA20'], label='20-Day MA')
plt.plot(hist['MA50'], label='50-Day MA')
plt.legend()
plt.show()

import numpy as np

def detect_inflection_points(hist):
    # Calculate the first derivative of the closing prices
    hist['First_Derivative'] = np.gradient(hist['Close'])
    
    # Calculate the second derivative of the closing prices
    hist['Second_Derivative'] = np.gradient(hist['First_Derivative'])
    
    # Identify inflection points where the second derivative changes sign
    inflection_points = hist[(hist['Second_Derivative'].shift(1) * hist['Second_Derivative'] < 0)]
    
    return inflection_points

# Example usage
inflection_points = detect_inflection_points(hist)
print(inflection_points)

# Plot the data with inflection points
plt.figure(figsize=(10, 5))
plt.plot(hist['Close'], label='Close Price')
plt.plot(hist['MA20'], label='20-Day MA')
plt.plot(hist['MA50'], label='50-Day MA')
plt.scatter(inflection_points.index, inflection_points['Close'], color='red', label='Inflection Points')
plt.legend()
plt.show()
