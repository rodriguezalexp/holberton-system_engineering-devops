#!/usr/bin/python3
""""""
import requests


def top_ten(subreddit):
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64)\
                                               AppleWebKit/537.36 \
                   (KHTML, like Gecko) Chrome/98.0.4758.87 Safari/537.36"}

    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.\
           format(subreddit)
    pop = requests.get(url, headers=headers, allow_redirects=False)
    poppop = pop.json().get('data').get('children')

    if pop.status_code == 200:
        for i in poppop:
            print(i.get('data').get('title'))
    else:
        print("None")
