import requests
import json
import urllib.parse

def post_discord(hook :str, msg :str) -> None:
    main_content = {'content': msg}
    headers = {'Content-Type': 'application/json'}
    requests.post(hook, json.dumps(main_content), headers=headers)

def get_tweet_url(text :str) -> str:
    url = "https://twitter.com/intent/tweet?text="
    url += urllib.parse.quote(text)
    return url