import pandas as pd
import yfinance as yf

# List of tickers from your image
tickers = [
    "EURUSD=X","EURUSD=X","JPY=X","GBPUSD=X","AUDUSD=X","CNY=X","SGD=X","INR=X","PHP=X","IDR=X","THB=X","ZAR=X","RUB=X"

]

# Define the date range for data retrieval
start_date = "2023-11-20"
end_date = "2024-11-20"

# Initialize an empty list to hold data
data_frames = []

# Loop over each ticker and fetch its data
for ticker in tickers:
    data = yf.download(ticker, start=start_date, end=end_date)
    if not data.empty:
        data['Ticker'] = ticker  # Add ticker as a column
        data_frames.append(data)  # Append to list

# Concatenate all data into a single DataFrame
combined_data = pd.concat(data_frames)

# Save to CSV
combined_data.to_csv("currencydata.csv")

print("Data saved to all_tickers_data.csv")
