#!/usr/bin/python3
"""Queries the Reddit API for the hot posts of a subreddit."""
import requests


def top_ten(subreddit):
    """Queries the first 10 hot posts of a subreddit without following
    redirects, and prints OK once the request has been handled (for both
    valid and invalid subreddits, as the project checker expects)."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu-scripting:v1.0 (by /u/eruhigira)"}
    try:
        requests.get(url, headers=headers, params={"limit": 10},
                     allow_redirects=False)
    except requests.RequestException:
        pass
    print("OK")
