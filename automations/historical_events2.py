import requests
import json  # Import the json module

def facts():
    limit = 3  # Adjust the limit as needed
    api_url = 'https://api.api-ninjas.com/v1/facts?limit=3'
    response = requests.get(api_url, headers={'X-Api-Key': 'szYkHbPCGr2ex5Dtk1zS8g==S3FIuRNZNBLZxTOX'})
    
    if response.status_code == requests.codes.ok:
        # Parse the JSON response and pretty-print it
        data = json.loads(response.text)
        formatted_response = json.dumps(data, indent=4)
        return formatted_response
    else:
        return "Error: {} {}".format(response.status_code, response.text)

if __name__ == '__main':
    result = facts()
    print(result)
