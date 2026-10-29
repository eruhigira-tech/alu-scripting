#!/usr/bin/python3
"""Recursively counts keywords in the hot post titles of a subreddit."""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Prints a sorted count of the given keywords found in hot titles."""
    if counts is None:
        counts = {}
    wanted = [word.lower() for word in word_list]
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu-scripting:v1.0 (by /u/eruhigira)"}
    params = {"limit": 100}
    if after:
        params["after"] = after
    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code != 200:
            return print_counts(counts, wanted)
        data = response.json().get("data", {})
    except (requests.RequestException, ValueError):
        return print_counts(counts, wanted)

    for post in data.get("children", []):
        title = post.get("data", {}).get("title") or ""
        for token in title.lower().split():
            if token in wanted:
                counts[token] = counts.get(token, 0) + 1
    after = data.get("after")
    if after:
        return count_words(subreddit, word_list, after, counts)
    print_counts(counts, wanted)


def print_counts(counts, wanted):
    """Prints counts (times duplicates in the list), sorted as required."""
    results = [(word, total * wanted.count(word))
               for word, total in counts.items()]
    for word, total in sorted(results, key=lambda x: (-x[1], x[0])):
        print("{}: {}".format(word, total))
