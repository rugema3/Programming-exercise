import requests
import config

def historicals(topic):
    """This function will handle historical events by calling the api_ninjas 
    args:
        topic: the topic to search for
    """
    url = 'https://api.api-ninjas.com/v1/historicalevents/'
    token = {'X-Api-Key': config.api_ninjas }
    params = {'text': topic}
    print(f"Request URL: {url}")
    print(f"Request Params: {params}")
    result = requests.get(url, headers=token, params=params)
    print(f"Response Status Code: {result.status_code}")
    print(f"Response Text: {result.text}")
    return result.text

def read_posted_topics():
    # Read the list of topics that have been posted and return it
    with open('posted_topics.txt', 'r') as file:
        return file.read().splitlines()

def write_posted_topic(topic):
    # Write the topic to the list of posted topics
    with open('posted_topics.txt', 'a') as file:
        file.write(topic + '\n')

if __name__ == '__main':
    topics = ['microsoft', 'apple', 'bitcoin']
    posted_topics = read_posted_topics()

    for topic in topics:
        if topic not in posted_topics:
            response = historicals(topic)
            #post_on_linkedin(response)  # Call your LinkedIn posting function
            write_posted_topic(topic)
            posted_topics.append(topic)  # Append the posted topic to the list
        print(response)  # Move this line outside of the if block to print the response

    print("Finished processing topics.")

