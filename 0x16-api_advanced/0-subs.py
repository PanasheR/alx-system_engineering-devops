#!/usr/bin/python3
"""Script to query Reddit using API"""
import requests


def number_of_subscribers(subreddit):
    """function queries Reddit API and returns subscribers"""

    red = requests.get("https://www.reddit.com/r/{}/about.json"
                       .format(subreddit))
    if red.status_code >= 300:
        return 0

    return red.json().get("data").get("subscribers")
