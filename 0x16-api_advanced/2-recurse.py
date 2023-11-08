#!/usr/bin/python3
"""
0x16. API advanced
"""

import requests


def recurse(subreddit):
    """The main function that is used to call the helper."""
    hot_list = []
    if not subreddit or not isinstance(subreddit, str):
        return None
    def recurse_helper(subreddit, after=None):
        """A recursive function that returns a list of all hot
        post's titles for a given subreddit."""
        nonlocal hot_list
        params = {"after": after} if after else {}
        response = requests.get(
            "https://reddit.com/r/{}/hot.json".format(subreddit),
            headers={"User-Agent": "custom"},
            params=params,
            allow_redirects=F
        )
        if response.status_code == 200:
            for item in response.json()["data"]["children"]:
                hot_list.append(item["data"]["title"])
            after = response.json()["data"]["after"]
            if after:
                recurse_helper(subreddit, after)
        else:
            return None

    recurse_helper(subreddit)
    return hot_list if hot_list else None
