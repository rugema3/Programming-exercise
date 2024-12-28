import requests
import config

def historicals(topic, year=2000, offset=4):
    """
    This function retrieves historical events related to a specific topic within a specified year.

    Args:
        topic (str): The topic you want to search for.
        year (int): The year for the search (default is 2000).
        offset (int): The number of results to retrieve (default is 4).
    """
    if not topic:
        print("Please provide a valid topic for the search.")
        return
    
    url = 'https://api.api-ninjas.com/v1/historicalevents/'
    token = {'X-Api-Key': config.api_ninjas }
    params = {'text': topic, 'year': year, 'offset': offset}
    
    try:
        result = requests.get(url, headers=token, params=params)
        result.raise_for_status()  # Raise an exception if the response status code is not 200
        events = result.json()
        
        print("\nHistorical events related to '{}' in the year {}:\n".format(topic, year))
        for event in events:
            print("Date: {}-{}-{}".format(event['year'], event['month'], event['day']))
            print("Event: {}\n".format(event['event']))
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve historical events: {e}")
    except ValueError as e:
        print(f"Failed to parse response as JSON: {e}")

if __name__ == '__main__':
    text = input("Please enter the topic you want to look up: ")
    year = input("Please enter the year: ")
    offset = input("How many results do you want? ")
    historicals(text, year, offset)

