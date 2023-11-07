#!/usr/bin/python3
"""
0x16. API advanced
"""
import requests


def top_ten(subreddit):
    """A function function that queries the Reddit API and prints the
    titles of the first 10 hot posts listed for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(
        url, headers={"User-Agent": "custom"}, params={"Max-Results": 10}
    )
    if response.status_code == 200:
        for data in response.json()["data"]["children"]:
            print(data["data"]["title"])
    else:
        return 0
