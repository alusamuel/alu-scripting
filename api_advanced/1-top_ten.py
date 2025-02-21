#!/usr/bin/python3
"""DOCS"""
import requests


def top_ten(subreddit):
    """Docs"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 10}
    
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code != 200:
        print(None)
        return
    
    try:
        data = response.json()
        posts = data['data']['children']
        
        for post in posts:
            print(post['data']['title'])
    except (KeyError, ValueError):
        print(None)
