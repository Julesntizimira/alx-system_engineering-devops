#!/usr/bin/python3
"""defines top_ten()"""
from requests import get


def top_ten(subreddit):
    """ prints the titles of the first 10 hot posts
        listed for a given subreddit."""
    if subreddit is None or not isinstance(subreddit, str):
        print(None)
        return
    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = 'https://www.reddit.com/r/{}.json'.format(subreddit)
    response = get(url, headers=user_agent)
    if response.status_code != '200':
        print(None)
        return
    results = response.json()
    try:
        res = results.get('data').get('children')
        i = 0
        for ps in res:
            if i >= 10:
                break
            print(ps.get('data').get('title'))
            i += 1
    except Exception:
        return print(None)
