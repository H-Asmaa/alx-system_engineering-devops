#!/usr/bin/python3
"""
0x16. API advanced
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """A recursive function that returns a list of all hot
    post's titles for a given subreddit."""
    params = {"after": after} if after else {}
    response = requests.get(
        "https://reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "custom"},
        params=params,
    )
    if response.status_code == 200:
        for item in response.json()["data"]["children"]:
            hot_list.append(item["data"]["title"])
        after = response.json()["data"]["after"]
        return (
            recurse(subreddit, hot_list, after) if after else hot_list
        )
    else:
        return None
