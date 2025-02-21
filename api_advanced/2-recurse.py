#!/usr/bin/python3
"""
Recursive Reddit Post Fetcher Module

Recursively retrieves all hot posts from a subreddit using pagination.

Functions:
    recurse(subreddit, hot_list=[], after=None)
        Recursively accumulates post titles
"""
import requests

def recurse(subreddit, hot_list=None, after=None):
    """
    Recursive hot post title collector
    
    Args:
        subreddit (str): Subreddit to query
        hot_list (list): Internal accumulation list
        after (str): Pagination token for next page
        
    Returns:
        list/None: List of post titles or None if invalid
        
    Notes:
        - Implements recursive pagination handling
        - Uses Reddit's 'after' parameter for pagination
        - Returns None if subreddit is invalid
    """
    if hot_list is None:
        hot_list = []
    headers = {'User-Agent': 'MyBot/0.0.1'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'after': after} if after else {}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code != 200:
        return None if not hot_list else hot_list
    data = response.json().get('data', {})
    posts = data.get('children', [])
    for post in posts:
        hot_list.append(post.get('data', {}).get('title'))
    next_after = data.get('after')
    if next_after:
        return recurse(subreddit, hot_list, next_after)
    return hot_list if hot_list else None
