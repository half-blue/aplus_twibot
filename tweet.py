import tweepy

from typing import Tuple


def auth_twitterAPI(BEARER_TOKEN: str, API_KEY: str, API_SECRET: str, ACCESS_TOKEN: str, ACCESS_TOKEN_SECRET: str) -> tweepy.Client:
    """OAuthを行いTweepyのAPIオブジェクトを返す"""
    client = tweepy.Client(
        bearer_token=BEARER_TOKEN,
        consumer_key=API_KEY,
        consumer_secret=API_SECRET,
        access_token=ACCESS_TOKEN,
        access_token_secret=ACCESS_TOKEN_SECRET,
        wait_on_rate_limit=False,
    )
    return client


def get_thread_url(thread_id: int) -> str:
    """スレッドIDからスレッドのURLを返す"""
    return f"https://www.aplus-tsukuba.net/threads/{thread_id}/"


def trim_text(text: str) -> str:
    """質問本文を50字にトリムする"""
    if len(text) > 50:
        return text[:49] + "…"
    else:
        return text


def tweet(client: tweepy.Client, trimed_text: str, url: str) -> None:
    """ツイートする"""
    msg = "A+つくばに新しい質問が投稿されました！\n----------\n"
    msg += trimed_text + "\n"
    msg += url
    client.create_tweet(text=msg)


def tweet_posts(api: tweepy.API, posts: Tuple[Tuple[str, int]]) -> None:
    """問い合わせ結果をツイートする"""
    for text, tid in posts:
        url = get_thread_url(tid)
        trimed_text = trim_text(text)
        tweet(api, trimed_text, url)
