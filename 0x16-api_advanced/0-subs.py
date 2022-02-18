#!/usr/bin/python3
"""Querie to the reddit API"""

import requests


def number_of_subscribers(subreddit):
    """function that queries the Reddit API 
    and returns the number of subscribers
    """
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64)\
                                           AppleWebKit/537.36 \
               (KHTML, like Gecko) Chrome/98.0.4758.87 Safari/537.36"}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    query = requests.get(url, headers=headers, allow_redirects=False)
    if query.status_code == 200:
        final = query.json().get('data').get('subscribers')
        return final
    return 0
