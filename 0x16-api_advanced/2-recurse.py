#!/usr/bin/python3
"""queires the reddit api 
   and returns a list containing the titles of all hot articles
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """recursive function that queires reddit api """
    url = "https://api.reddit.com/r/{}?sort=hot".format(subreddit)
    headers = {'User-Agent': 'CustomClient/1.0'}
    params = {"limit": 100, "after": after} if after else {"limit": 100}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        after = data["data"]["after"]
        for post in posts:
            hot_list.append(post["data"]["title"])
        if after:
            recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None

