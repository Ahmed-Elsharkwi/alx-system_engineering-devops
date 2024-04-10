#!/usr/bin/python3
"""
Get the top ten titles of posts
"""


import requests


def top_ten(subreddit):
    """ return the number of subscribers """

    headers = {'User-Agent': 'Mozilla/5.0'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        dic = response.json().get("data")
        posts = dic["children"]
        counter = 0
        for dict in posts:
            if counter < 10:
                print(dict["data"]["title"])
                counter += 1

    else:
        print(None)
