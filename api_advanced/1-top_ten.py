#!/usr/bin/python3
"""
1-top_ten
"""
import requests

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyBot/0.0.1'}
    params = {'limit': 10}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    data = response.json().get('data', {})
    posts = data.get('children', [])
    for post in posts:
        print(post.get('data', {}).get('title'))
