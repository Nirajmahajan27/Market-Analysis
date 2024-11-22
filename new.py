import requests
import pandas as pd
from datetime import datetime

# List of cryptocurrencies with their CoinGecko IDs
cryptos = [
    {"symbol": "HAMSTER", "id": "hamster"},
    {"symbol": "BABYDOGE", "id": "baby-doge-coin"}
]

# API endpoint
base_url = "https://api.coingecko.com/api/v3/coins/{id}/market_chart/range"

# Define the date range
start_date = "2023-01-01"
end_date = "2023-12-31"
start_timestamp = int(datetime.strptime(start_date, "%Y-%m-%d").timestamp())
end_timestamp = int(datetime.strptime(end_date, "%Y-%m-%d").timestamp())

# Prepare the data
data_frames = []

for crypto in cryptos:
    url = base_url.format(id=crypto["id"])
    params = {
        "vs_currency": "usd",
        "from": start_timestamp,
        "to": end_timestamp
    }
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            prices = pd.DataFrame(data["prices"], columns=["Timestamp", "Adj Close"])
            market_caps = pd.DataFrame(data["market_caps"], columns=["Timestamp", "Market Cap"])
            volumes = pd.DataFrame(data["total_volumes"], columns=["Timestamp", "Volume"])

            # Merge data into one DataFrame
            df = prices.merge(volumes, on="Timestamp")
            df["Symbol"] = crypto["symbol"]
            df["Date"] = pd.to_datetime(df["Timestamp"], unit="ms").dt.date
            df["Open"] = df["Adj Close"]
            df["High"] = df["Adj Close"]
            df["Low"] = df["Adj Close"]

            # Reorder columns
            df = df[["Symbol", "Date", "Open", "High", "Low", "Adj Close", "Volume"]]
            data_frames.append(df)
        else:
            print(f"Failed to fetch data for {crypto['symbol']}: {response.status_code}")
    except Exception as e:
        print(f"Error fetching data for {crypto['symbol']}: {e}")

# Combine all data and save to CSV
if data_frames:
    combined_data = pd.concat(data_frames, ignore_index=True)
    combined_data.to_csv("crypto_data.csv", index=False)
    print("Data saved to crypto_data.csv")
else:
    print("No data fetched!")
