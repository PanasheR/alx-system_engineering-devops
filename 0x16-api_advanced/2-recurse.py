#!/usr/bin/python3
"""recursive function that queries the Reddit API and returns
   a list containing the titles of all hot articles for a
   given subreddit. If no results are found for the given
   subreddit, the function should return None."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """"""
    try:
        rd = requests.get("https://www.reddit.com/r/{}/hot.json".
                          format(subreddit),
                          headers={"User-Agent": "custom"},
                          params={"after": after},
                          allow_redirects=False).json()
    except None:
        return None

    if ("data" in rd and "children" in rd.get("data")):
        for j in rd.get("data").get("children"):
            hot_list.append(j.get("data").get("title"))
        if "after" in rd.get("data") and rd.get("data").get("after"):
            return recurse(subreddit, hot_list,
                           rd.get("data").get("after"))
        else:
            return hot_list
    else:
        return None
