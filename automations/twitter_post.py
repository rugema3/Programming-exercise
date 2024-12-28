import requests

url = "https://twitter.com/i/api/1.1/jot/client_event.json"

headers = {
            "Bearer": "AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA"
            }
payload = {
        "content" : "Posting from the commandline."
        }

result = requests.post(url, payload, headers=headers)
print(result)
