#!/usr/bin/python3
"""
GET the number of subscribers of a specified subreddit
"""


import requests


def number_of_subscribers(subreddit):
    """ return the number of subscribers """

    headers = {'User-Agent': 'Mozilla/5.0'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        dic = response.json().get("data")
        return dic["subscribers"]

    else:
        return 0
