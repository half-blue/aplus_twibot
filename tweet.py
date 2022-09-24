import tweepy

from typing import Tuple


def get_thread_url(thread_id : int) -> str:
    """スレッドIDからスレッドのURLを返す"""
    return f"https://www.aplus-tsukuba.net/threads/{thread_id}/"

def trim_text(text :str) -> str:
    """質問本文を50字にトリムする"""
    if len(text) > 50:
        return text[:49] + "…"
    else:
        return text

def tweet(api: tweepy.API, trimed_text: str, url: str) -> None:
    """ツイートする"""
    msg = "A+つくばに新しい質問が投稿されました！\n----------\n"
    msg += trimed_text + "\n"
    msg += url
    api.update_status(msg)

def tweet_posts(api :tweepy.API, posts : Tuple[Tuple[str, int]]) -> None:
    """問い合わせ結果をツイートする"""
    for text, tid in posts:
        url = get_thread_url(tid)
        trimed_text = trim_text(text)
        tweet(api, trimed_text, url)

