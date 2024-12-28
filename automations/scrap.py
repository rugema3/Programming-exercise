import requests
from bs4 import BeautifulSoup

# Define the hashtag you want to search for
hashtag = 'RWANDA'

# Create the Twitter search URL
search_url = f'https://twitter.com/hashtag/{hashtag}?src=hashtag_click'

# Send an HTTP GET request to the search URL
response = requests.get(search_url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract and print the tweet text
    tweet_elements = soup.find_all('div', class_='css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0')
    for tweet_element in tweet_elements:
        tweet_text = tweet_element.get_text()
        print(tweet_text)
else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")
