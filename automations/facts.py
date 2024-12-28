import requests

def facts():
    """This fact function will return a random fact."""
    headers = {
        "X-Api-Key": "szYkHbPCGr2ex5Dtk1zS8g==S3FIuRNZNBLZxTOX"
    }
    url = "https://api.api-ninjas.com/v1/facts?limit=10"
    result = requests.get(url, headers=headers)

    if result.status_code == 200:
        data = result.json()  # Extract the JSON data from the response
        for fact in data:
            print(fact['fact'])  # Print each fact as plain text
    else:
        print(f"Request failed with status code: {result.status_code}")

if __name__ == '__main__':
    facts()

