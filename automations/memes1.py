import requests

def get_programming_meme_with_title(title=""):
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

            if title:
                hashtag_title = f"#{title.replace(' ', '_')}"  # Replace spaces with underscores
                return f"{hashtag_title}\n{meme_url}"

            return meme_url

        else:
            print("No memes found in the response.")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching meme: {e}")

if __name__ == '__main__':
    title = "Code Laughter Chronicles"
    meme_url_with_title = get_programming_meme_with_title(title)
    
    if meme_url_with_title:
        print(f"Meme URL with Title: {meme_url_with_title}")
    else:
        print("Failed to retrieve a meme URL.")

