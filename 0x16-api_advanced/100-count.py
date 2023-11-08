#!/usr/bin/python3
"""
0x16. API advanced
"""

import requests


def count_words(subreddit, word_list, dictionary={}, after=None):
    """A recursive function that queries the Reddit
    API  parses the title of all hot articles, and prints
    a sorted count of given keywords (case-insensitive,
    delimited by spaces."""
    if not subreddit or not isinstance(subreddit, str):
        print()
    params = {"after": after} if after else {}
    response = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "costum"},
        params=params,
        allow_redirects=False
    )
    if response.status_code == 200:
        if response.json()["data"]:
            data = response.json()["data"]
            for item in data["children"]:
                for word in word_list:
                    if word.lower() in item["data"]["title"].lower():
                        title = item["data"]["title"].lower()
                        dictionary[word.lower()] = dictionary.get(
                            word.lower(), 0
                            ) + 1
            if data["after"]:
                return count_words(
                    subreddit, word_list, dictionary, after=data["after"]
                )
            else:
                sortedDict = dict(
                    sorted(dictionary.items(), key=lambda item: (-item[1],
                                                                 item[0]))
                )
                for key, val in sortedDict.items():
                    print("{}: {}".format(key, val))
    elif response.status_code == 429:
        print("Blati ra l9adiya mamslkach db!")
    else:
        print(f"Error {response.status_code}")
        return None
