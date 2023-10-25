import requests

url = "https://programming-memes-images.p.rapidapi.com/v1/memes"

headers = {
    "X-RapidAPI-Key": "45b382a8e4mshbba0ee82166d09ap12283ajsn18194730869a",
    "X-RapidAPI-Host": "programming-memes-images.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

data = response.json()
if 'memes' in data:
    memes = data['memes']
    for index, meme in enumerate(memes):
        image_url = meme['url']
        response = requests.get(image_url)
        with open(f'meme{index}.jpg', 'wb') as f:
            f.write(response.content)

