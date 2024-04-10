#!/usr/bin/python3
"""
GET the number of subscribers of a specified subreddit
"""
import requests

def number_of_subscribers(subreddit):
    "anthing"
    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(f'https://www.reddit.com/r/{subreddit}/about.json', headers=headers)

    if response.status_code == 200:
        return response.json()['data']['subscribers']
    else:
        return 0

