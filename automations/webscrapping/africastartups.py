from bs4 import BeautifulSoup
import requests

url = 'https://www.newtimes.co.rw/elections'
response = requests.get(url)
print(response.status_code)
soup = BeautifulSoup(response.text, 'html.parser')

print(soup.find_all('div'))