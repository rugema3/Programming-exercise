import requests
from bs4 import BeautifulSoup

# Define the search parameters
query = "rwanda since:2022-01-01 until:2022-12-31"
url = f"https://twitter.com/search?q={query}&src=typd"

# Send an HTTP GET request to the Twitter search URL
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Example: Extract and print the tweets
    tweet_elements = soup.find_all("div", class_="tweet-text")
    for tweet in tweet_elements:
        print(tweet.text)

else:
    print(f"An error occurred during the HTTP request. Status code: {response.status_code}")

