#!/usr/bin/python3
"""function that queries the Reddit API and prints the titles
   of the first 10 hot posts listed for a given subreddit"""
import requests


def top_ten(subreddit):
    """function returns titles"""
    rd = requests.get("https://reddit.com/r/{}.json?sort=hot&limit=10".
                      format(subreddit), headers={"User-Agent": "custom"})

    if (rd.status_code == 200):
        for j in rd.json().get("data").get("children"):
            print(j.get("data").get("title"))
    else:
        print("None")
