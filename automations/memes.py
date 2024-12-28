import requests

def get_programming_meme():
    url = "https://programming-memes-images.p.rapidapi.com/v1/memes"

    headers = {
        "X-RapidAPI-Key": "45b382a8e4mshbba0ee82166d09ap12283ajsn18194730869a",
        "X-RapidAPI-Host": "programming-memes-images.p.rapidapi.com"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        meme_data_list = response.json()

        if meme_data_list:
            first_meme_data = meme_data_list[0]
            meme_url = first_meme_data.get('image')
            return meme_url

        else:
            print("No memes found in the response.")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching meme: {e}")

if __name__ == '__main__':
    meme_url = get_programming_meme()
    if meme_url:
        print(f"Meme URL: {meme_url}")
    else:
        print("Failed to retrieve a meme URL.")

