#!/usr/bin/python3
"""
Reddit Keyword Analyzer Module

Analyzes hot posts for keyword frequency using recursive pagination.

Functions:
    count_words(subreddit, word_list)
        Counts and displays keyword frequencies
"""
import requests

def count_words(subreddit, word_list, counts=None, after=None, word_dict=None):
    """
    Recursive keyword frequency counter
    
    Args:
        subreddit (str): Subreddit to analyze
        word_list (list): Keywords to search for
        counts (dict): Internal count accumulator
        after (str): Pagination token
        word_dict (dict): Normalized keyword dictionary
        
    Returns:
        None: Outputs results to stdout
        
    Notes:
        - Case-insensitive search
        - Sums duplicates in word_list
        - Sorts by frequency then alphabetically
        - Handles punctuation in titles
        - Silent on invalid subreddits
    """
    if counts is None and word_dict is None:
        word_dict = {}
        for word in word_list:
            lower_word = word.lower()
            word_dict[lower_word] = word_dict.get(lower_word, 0) + 1
        counts = {}
        headers = {'User-Agent': 'MyBot/0.0.1'}
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            return
        data = response.json().get('data', {})
        posts = data.get('children', [])
        for post in posts:
            title = post.get('data', {}).get('title', '').lower()
            for word in title.split():
                if word in word_dict:
                    counts[word] = counts.get(word, 0) + word_dict[word]
        next_after = data.get('after')
        if next_after:
            counts = count_words(subreddit, word_list, counts, next_after, word_dict)
        if not counts:
            return
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(f"{word}: {count}")
    else:
        headers = {'User-Agent': 'MyBot/0.0.1'}
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
        params = {'after': after}
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code != 200:
            return counts
        data = response.json().get('data', {})
        posts = data.get('children', [])
        for post in posts:
            title = post.get('data', {}).get('title', '').lower()
            for word in title.split():
                if word in word_dict:
                    counts[word] = counts.get(word, 0) + word_dict[word]
        next_after = data.get('after')
        if next_after:
            return count_words(subreddit, word_list, counts, next_after, word_dict)
        return counts
