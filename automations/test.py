import requests

url = "https://animals-by-api-ninjas.p.rapidapi.com/v1/animals"

querystring = {"name": "pig"}

headers = {
    "X-RapidAPI-Key": "45b382a8e4mshbba0ee82166d09ap12283ajsn18194730869a",
    "X-RapidAPI-Host": "animals-by-api-ninjas.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

data = response.json()

for animal in data:
    print(f"Name: {animal['name']}")
    
    characteristics = animal.get('characteristics', {})
    
    common_name = characteristics.get('common_name', 'N/A')
    
    print(f"Common Name: {common_name}")
    print(f"Location: {', '.join(animal['locations'])}")
    print(f"Habitat: {characteristics.get('habitat', 'N/A')}")
    print(f"Diet: {characteristics.get('diet', 'N/A')}")
    print(f"Top Speed: {characteristics.get('top_speed', 'N/A')}")
    print(f"Lifespan: {characteristics.get('lifespan', 'N/A')}")
    print(f"Weight: {characteristics.get('weight', 'N/A')}")
    print("-" * 50)

