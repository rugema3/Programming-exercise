import requests
import datetime

def get_historical_events(month, day):
    """
    Fetches historical events, births, and deaths for a given month and day from Wikipedia's On This Day API.

    Args:
        month (int): The month (1-12).
        day (int): The day of the month (1-31).

    Returns:
        dict: A dictionary containing events, births, and deaths for the given date.
    """
    url = f"https://en.wikipedia.org/api/rest_v1/feed/onthisday/all/{month}/{day}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  
        data = response.json()
        
        # Organize the data into categories
        results = {
            "events": data.get("events", []),
            "births": data.get("births", []),
            "deaths": data.get("deaths", [])
        }
        return results

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

# Example Usage
if __name__ == "__main__":
    # Get todays date
    today = datetime.date.today()   
    month = today.month 
    day = today.day  
    historical_data = get_historical_events(month, day)
    
    if historical_data:
        print("Historical Events:")
        for event in historical_data["events"]:
            print(f"- {event['year']}: {event['text']}")
        
        print("\nFamous Births:")
        for birth in historical_data["births"]:
            print(f"- {birth['year']}: {birth['text']}")
        
        print("\nNotable Deaths:")
        for death in historical_data["deaths"]:
            print(f"- {death['year']}: {death['text']}")
