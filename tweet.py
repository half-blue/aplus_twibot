import tweepy

from typing import Tuple

from discord import post_discord, get_tweet_url

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

def tweet(client: tweepy.Client, trimed_text: str, url: str, webhook_url :str) -> None:
    """ツイートする"""
    msg = "A+つくばに新しい質問が投稿されました！\n----------\n"
    msg += trimed_text + "\n"
    msg += url
    try:
        client.create_tweet(text=msg)
    except:
        url = get_tweet_url(msg)
        discord_msg = "手動で投稿してください．投稿後に :thumbsup: をお願いします．\n"
        discord_msg += url
        post_discord(webhook_url, discord_msg)


def tweet_posts(api: tweepy.API, posts: Tuple[Tuple[str, int]], webhook_url: str) -> None:
    """問い合わせ結果をツイートする"""
    for text, tid in posts:
        url = get_thread_url(tid)
        trimed_text = trim_text(text)
        tweet(api, trimed_text, url, webhook_url)
            
