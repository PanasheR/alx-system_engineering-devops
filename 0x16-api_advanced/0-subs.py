#!/usr/bin/python3
"""Querying Reddit API"""
import requests


def number_of_subscribers(subreddit):
    """function that queries the Reddit API and returns the number
       of subscribers"""

    result = requests.get("https://www.reddit.com/r/{}/about.json"
                          .format(subreddit))
    if result.status_code >= 300:
        return 0

    return result.json().get("data").get("subscribers")
