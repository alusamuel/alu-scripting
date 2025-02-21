#!/usr/bin/python3
"""
Reddit Keyword Analyzer Module

Analyzes hot posts for keyword frequency using recursive pagination.

Functions:
    count_words(subreddit, word_list)
        Counts and displays keyword frequencies
"""
import sys

if __name__ == '__main__':
    count_words = __import__('3-count').count_words
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        result = count_words(sys.argv[1], [x for x in sys.argv[2].split()])
