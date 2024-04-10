#!/usr/bin/python3
"""
returns a list containing the titles of all hot articles
"""


import requests


def recurse(subreddit, hot_list=[], after=""):
    """returns a list containing the titles of all hot articles """

    headers = {'User-Agent': 'Mozilla/5.0'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    response = requests.get(url, headers=headers, params={'after':after})

    if response.status_code == 200:
        dic = response.json().get("data")
        posts = dic["children"]
        if after is None:
            return hot_list
        else:
            for post in posts:
                hot_list.append(post['data']['title'])
            after = dic['after']
            return recurse(subreddit, hot_list, after)
    else:
        return None
