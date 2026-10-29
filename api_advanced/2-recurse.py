#!/usr/bin/python3
"""Recursively collects the titles of all hot posts of a subreddit."""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """Returns a list of all hot post titles, or None if invalid subreddit."""
    if hot_list is None:
        hot_list = []
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu-scripting:v1.0 (by /u/eruhigira)"}
    params = {"limit": 100}
    if after:
        params["after"] = after
    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code != 200:
            return hot_list if hot_list else None
        data = response.json().get("data", {})
    except (requests.RequestException, ValueError):
        return hot_list if hot_list else None

    for post in data.get("children", []):
        hot_list.append(post.get("data", {}).get("title"))
    after = data.get("after")
    if after:
        return recurse(subreddit, hot_list, after)
    return hot_list
