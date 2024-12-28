import config
import requests
import jokes
import os
from today_in_history import get_historical_events
import datetime
from discord import discord_post_general

access_token = config.LINKEDIN_ACCESS_TOKEN
user_id = config.USER_ID

class SocialMediaAutomator:
    """
    A class for automating social media posts.

    This class provides methods for posting content on social media platforms.

    Attributes:
        access_token (str): The access token for the social media platform.
        user_id (str): The user ID for the social media platform.
        post_url (str): The URL for posting content on the platform.
    """
    
    def __init__(self):
        """
        Initialize the SocialMediaAutomator with the access token, user ID, and post URL.
        """
        # Load values from social.env
        self.access_token = access_token
        self.user_id = user_id
        self.post_url = 'https://api.linkedin.com/v2/ugcPosts'
       
    def create_post(self, post_content, visibility='PUBLIC'):
        """
        Create a post on the social media platform.

        Args:
            post_content (str): The content of the post.
            visibility (str, optional): The visibility setting for the post. Defaults to 'PUBLIC'.

        Returns:
            str: A message indicating the result of the post creation.
        """
        post_data = {
            "author": "urn:li:person:nJ_-mjF6B5",
            "lifecycleState": "PUBLISHED",
            "specificContent": {
                "com.linkedin.ugc.ShareContent": {
                    "shareCommentary": {
                        "text": post_content
                    },
                    "shareMediaCategory": "NONE"
                }
            },
            "visibility": {
                "com.linkedin.ugc.MemberNetworkVisibility": visibility
            }
        }
        
        headers = {
            'Authorization': 'Bearer ' + self.access_token,
            'Content-Type': 'application/json',
        }
        
        response = requests.post(self.post_url, headers=headers, json=post_data)
        
        if response.status_code == 201:
            return "Post was successful."
        else:
            return f"Post failed with status code: {response.status_code}"
        
def format_for_linkedin(events, character_limit=2800):
    """
    Formats historical events for a LinkedIn post, ensuring it stays within the character limit.
    Args:
        events (list): List of events as returned by the API.
        character_limit (int): Maximum number of characters allowed for the LinkedIn post.
    Returns:
        str: A formatted string of events.
    """
    # Get today's date and months
    today = datetime.date.today()
    day = today.day
    month_name = today.strftime("%B")
    post_content = f"🌟 Historical Events for Today ({month_name} {day} in history):\n\n"
    char_count = len(post_content)

    for event in events:
        year = event.get("year", "Unknown year")
        description = event.get("text", "")
        entry = f"📜 {year}: {description}\n"
        
        if char_count + len(entry) <= character_limit:
            post_content += entry
            char_count += len(entry)
        else:
            post_content += "\n.#History #OnThisDay #WorldEvents #HistoricalEvents #Knowledge #Learning #Facts #Education #Discover #Explore #CulturalHeritage #GlobalHistory"
            break

    return post_content

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    social_media_automator = SocialMediaAutomator()

    today = datetime.date.today()
    month = today.month 
    day = today.day  
    historical_data = get_historical_events(month, day)
    
    
    if historical_data:
        post_content = format_for_linkedin(historical_data['events'])
        print(f"length of content: {len(post_content)}")
        print()
        print(f"post content: {post_content}")

        result = social_media_automator.create_post(post_content)
    
        print(result)

    # Post on Discord
    """
    try:
        message = jokes.get_programming_joke()
        print(message)
        result = discord_post_general(message)
        print(f"result: {result}")
    except Exception as e:
        print(f"Failed to post: {str(e)}")
        """