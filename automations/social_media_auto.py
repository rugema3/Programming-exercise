import config
import requests
import jokes
import os

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

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    social_media_automator = SocialMediaAutomator()
    
    post_content = jokes.get_programming_joke()
    
    result = social_media_automator.create_post(post_content)
    
    print(result)

