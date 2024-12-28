import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

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

# Grouped Bar Chart
dates = dataframes[currencies[0]].index
bar_width = 0.25
bar_positions = np.arange(len(dates))

plt.figure(figsize=(15, 8))
for i, (currency, df) in enumerate(dataframes.items()):
    plt.bar(bar_positions + i * bar_width, df['close'], width=bar_width, label=f'{base_currency}/{currency}')

plt.title(f'USD Performance Against Other Currencies (Grouped Bar Chart)')
plt.xlabel('Date')
plt.ylabel('Exchange Rate')
plt.xticks(bar_positions + (len(currencies) - 1) * bar_width / 2, [date.strftime('%Y-%m-%d') for date in dates], rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save the chart as an image file
plt.savefig('grouped_bar_chart.png')

# Optional: Show a confirmation message
print('Grouped bar chart saved as grouped_bar_chart.png')

