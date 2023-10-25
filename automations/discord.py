#!/usr/bin/env python3
"""Post on discord module.
Description:
            This module will post a message on a discord channel.
            The API endpoints have been obtained using the inspect element
            where we get the url with the channel id as well.
            we also obtained the headers. We did not need to have a discord 
            app or read any of the discord api official documentation.

            We are importings the jokes module that fetches a random joke
            from the jokes api. the returned joke will be posted on a discord
            channel.

            The authorisation and the url because it contains sensitive info
            has been saved in a module called config.py that won't be pushed 
            on github.
"""

import requests
import config # the file that contains the headers for auntentication.
import jokes # contains the jokes obtained from the jokes api.
authorisation = config.authorisation
end_point = config.url # Url for the cohort_13 channel discord
url_review = config.url_review # url for the cohort_13 review channel
url_kigali = config.url_kigali # url for the Kigali channel Software engineers
url_general = config.url_general # URL for the general Channel


def discord_post(msg):
    """This function will post the message on a discord channel.
    args:
        msg : message to be posted on the channel.
    """
    url = end_point

    payload = {
            "content" : msg
            }
    headers = {
            "Authorization": authorisation
            }
    result = requests.post(url, payload, headers=headers)
    print(result)

def discord_post_review(msg):
    """This function will post the message ona  discord channel.
    The name of the channel is cohort_13 review. This is a discord channel
    of ALX_Africa software engineering students.

    args:
        msg: message to be posted on the channel.
    """
    url = url_review
    payload = {
            "content" : msg
            }
    headers = {
            "Authorization": authorisation
            }
    result = requests.post(url, payload, headers=headers)
    print(result)

def discord_post_general(msg):
    """This function will post on the channel called general.
    args:
            msg : message to be posted.

    """
    url = url_general
    
    payload = {
            "content" : msg
            }
    headers = {
            "Authorization": authorisation
            }
    result = requests.post(url, payload, headers=headers)
    print(result)


def discord_post_kigali(msg):
    """Post of Kigali Channel.
    args:
            msg:    message to be posted
    """
    url = url_kigali
    payload = {
            "content" : msg
            }
    headers = {
            "Authorization": authorisation
            }
    result = requests.post(url, payload, headers=headers)
    print(result)


if __name__ == '__main__':
    msg = jokes.get_programming_joke()
    discord_post(msg)
    discord_post_kigali(msg)
    discord_post_review(msg)
    discord_post_general(msg)
