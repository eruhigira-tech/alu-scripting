# api_advanced

Python functions that query the Reddit API (no authentication, custom
User-Agent, redirects not followed).

| File | Description |
| --- | --- |
| `0-subs.py` | `number_of_subscribers(subreddit)`: subscriber count, 0 if invalid |
| `1-top_ten.py` | `top_ten(subreddit)`: prints first 10 hot titles, `None` if invalid |
| `2-recurse.py` | `recurse(subreddit, hot_list=None, after=None)`: all hot titles, recursively |
| `3-count.py` | `count_words(subreddit, word_list)`: recursive sorted keyword count |
