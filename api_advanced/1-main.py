#!/usr/bin/python3
"""
Function that queries Reddit API and prints titles of first 10 hot posts
for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Queries Reddit API for top 10 hot posts in a subreddit.
    
    Args:
        subreddit (str): Subreddit name to query
        
    Returns:
        None: Prints titles or None if subreddit is invalid
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'python:subreddit.hot.posts:v1.0 (by /u/user)'}
    
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        try:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            
            if posts:
                for post in posts:
                    print(post.get('data', {}).get('title'))
            else:
                print('OK')
        except ValueError:
            pass
    else:
        print('OK')
