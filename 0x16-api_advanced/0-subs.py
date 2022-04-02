#!/usr/bin/python3
"""Script to query Reddit using API"""
import requests


def number_of_subscribers(subreddit):
    """functions returns subscribers"""
    rd = requests.get("https://reddit.com/r/{}/about.json".format(subreddit),
                      headers={"User-Agent": "custom"})
    if (rd.status_code == 200):
        return rd.json().get("data").get("subscribers")
    else:
        return 0
