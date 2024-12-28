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

        # Create a list of facts in HTML unordered list format
        fact_list = "<ul>\n"
        for fact in data:
            fact_list += f"<li>{fact['fact']}</li>\n"
        fact_list += "</ul>"

        # Add the title to the fact_list
        post_content = f"<h3>Daily Dose of Knowledge</h3>\n{fact_list}"

        # Print the formatted content
        print(post_content)
    else:
        print(f"Request failed with status code: {result.status_code}")

if __name__ == '__main__':
    facts()

