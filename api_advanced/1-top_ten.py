#!/usr/bin/python3
"""Reddit API Query - Top 10 Hot Posts"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts from a subreddit"""
    reddit_url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyRedditBot/0.1 by YourUsername'}

    response = requests.get(reddit_url, headers=headers, allow_redirects=False)

    # Check if request is successful
    if response.status_code == 200:
        try:
            data = response.json().get('data', {})
            posts = data.get('children', [])

            if posts:
                for post in posts[:10]:
                    print(post['data']['title'])
            else:
                print(None)
        except (ValueError, KeyError):
            print(None)

    else:
        print(None)
