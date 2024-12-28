import requests
import config

token = config.authorisation
url = config.url_alfred

payload = {
        "content": "I will be waiting for your response."
        }

headers = {
        "Authorization" : config.authorisation
        }

result = requests.post(url, payload, headers=headers)
print(result)

