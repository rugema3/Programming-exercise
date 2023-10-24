import requests

def get_programming_joke():
    response = requests.get('https://v2.jokeapi.dev/joke/Programming?format=json')
    if response.status_code == 200:
        joke_data = response.json()
        if joke_data.get('type') == 'twopart':
            return f"JOKE OF THE DAY:\nQuestion: {joke_data['setup']}\nResponse: {joke_data['delivery']}"
        elif joke_data.get('type') == 'single':
            return f"JOKE OF THE DAY\n" + joke_data['joke']
        else:
            return "Failed to fetch a joke."
    else:
        return "Failed to fetch a joke."

if __name__ == "__main__":
    joke = get_programming_joke()
    print(joke)
