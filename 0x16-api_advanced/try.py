#!/usr/bin/python3
"""
Get the top ten titles of posts
"""


import requests


def top_ten(subreddit):
    """ return the number of subscribers """

    headers = {'User-Agent': 'Mozilla/5.0'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    response = requests.get(url, headers=headers, params={"after": "t3_1bzn0qx"})

    if response.status_code == 200:
        dic = response.json().get("data")
        posts = dic["children"]
        print(response.json())

    else:
        return None
top_ten("programming")
