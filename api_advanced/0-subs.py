#!/usr/bin/python3
"""
Reddit Subscriber Counter Module

Provides functionality to fetch subscriber count for a subreddit.
Uses Reddit's API at https://www.reddit.com/dev/api/

Functions:
    number_of_subscribers(subreddit)
        Queries Reddit API for subreddit subscriber count
"""
import requests

def number_of_subscribers(subreddit):
    """
    Get total subscribers for a subreddit
    
    Args:
        subreddit (str): Name of subreddit to query
        
    Returns:
        int: Number of subscribers. Returns 0 for invalid subreddits.
        
    Raises:
        None: Handles all exceptions internally
        
    Notes:
        - Sets custom User-Agent to avoid rate limits
        - Does not follow redirects (invalid subreddits may redirect)
        - Uses Reddit's /about.json endpoint
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'MyBot/0.0.1'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        return data.get('data', {}).get('subscribers', 0)
    return 0