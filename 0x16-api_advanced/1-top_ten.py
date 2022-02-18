#!/usr/bin/python3
"""list 10 hot subreddits"""

import requests


def top_ten(subreddit):
    """function to find post subreddits"""
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64)\
                                               AppleWebKit/537.36 \
                   (KHTML, like Gecko) Chrome/98.0.4758.87 Safari/537.36"}

    url = 'https://www.reddit.com/r/{}/hot.json?limit=10&g="GLOBAL"'.\
        format(subreddit)
    req_get = requests.get(url, allow_redirects=False, headers=headers)
    filter = req_get.json().get('data').get('children')

    if req_get.status_code == 200:
        for i in filter:
            print(i.get('data').get('title'))
    else:
        print("None")
