#!/usr/bin/python3
"""
Reddit Hot Posts Module

Retrieves and displays top 10 hot posts from a subreddit.

Functions:
    top_ten(subreddit)
        Prints titles of first 10 hot posts
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
