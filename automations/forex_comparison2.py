import requests
import pandas as pd
import matplotlib.pyplot as plt

# Replace 'YOUR_API_KEY' with your Alpha Vantage API key
api_key = 'U50RHCLKNOMTR1SC'
base_currency = 'USD'

# List of currencies to compare against USD
currencies = ['RWF', 'UGX', 'KES', 'TZS', 'BIF']

# Function to fetch forex data
def get_forex_data(api_key, base_currency, target_currency):
    url = f'https://www.alphavantage.co/query?function=FX_DAILY&from_symbol={base_currency}&to_symbol={target_currency}&apikey={api_key}'
    response = requests.get(url)
    data = response.json()

    # Extract time series data
    time_series = data.get('Time Series FX (Daily)')

    if time_series:
        df = pd.DataFrame(time_series).T
        df.index = pd.to_datetime(df.index)
        df.columns = ['open', 'high', 'low', 'close']
        df = df.astype(float)
        return df
    else:
        print(f"Failed to fetch data for {target_currency}. Error: {data.get('Note', 'Unknown error')}")
        return None

# Fetch forex data for each currency
dataframes = {}
for currency in currencies:
    df = get_forex_data(api_key, base_currency, currency)
    if df is not None:
        dataframes[currency] = df

# Print the data
for currency, df in dataframes.items():
    print(f"\nData for {base_currency}/{currency}:\n{df}")

# Plotting the data
plt.figure(figsize=(12, 6))
for currency, df in dataframes.items():
    plt.plot(df.index, df['close'], label=f'{base_currency}/{currency}')

plt.title(f'USD Performance Against Other Currencies')
plt.xlabel('Date')
plt.ylabel('Exchange Rate')
plt.legend()
plt.grid(True)

# Save the graph as a PNG file
plt.savefig('forex_comparison.png')

# Close the plot to avoid the warning
plt.close()

