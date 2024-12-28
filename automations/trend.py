from pytrends.request import TrendReq

# Create a pytrends object
pytrends = TrendReq(hl='en-US', tz=360)

# Set a general, non-specific keyword or keywords
keywords = ["technology", "innovation", "trends"]

# Build the payload
pytrends.build_payload(keywords, cat=0, timeframe='today 5-y', geo='', gprop='')

# Get interest over time
interest_over_time_df = pytrends.interest_over_time()

# Print the data
print(interest_over_time_df)

