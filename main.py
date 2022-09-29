import yaml
import MySQLdb
from MySQLdb import cursors
import tweepy

from lastrun import save_lastrun_datetime, load_lastrun_datetime
from inquire_newpost import inquire_new_posts, mysql_connect
from tweet import tweet_posts, auth_twitterAPI

import os
# cronで実行する場合、カレントディレクトリを動的に設定する必要がある。
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


def load_secrets() -> dict:
    """機密情報のyamlファイルを読み込み辞書データを返す"""
    with open("secret.yaml", "r") as f:
        yaml_dict = yaml.safe_load(f.read())
    return yaml_dict


if __name__ == "__main__":
    LAST_RUN_DT = load_lastrun_datetime()

    SECRETS = load_secrets()
    client = auth_twitterAPI(
        SECRETS["Twitter"]["BEARER_TOKEN"],
        SECRETS["Twitter"]["API_KEY"],
        SECRETS["Twitter"]["API_SECRET"],
        SECRETS["Twitter"]["ACCESS_TOKEN"],
        SECRETS["Twitter"]["ACCESS_TOKEN_SECRET"]
    )
    conn = mysql_connect(
        SECRETS["MySQL"]["User"],
        SECRETS["MySQL"]["Password"],
        SECRETS["MySQL"]["Host"],
        SECRETS["MySQL"]["Database"],
        SECRETS["MySQL"]["Port"]
    )
    cur: cursors.Cursor = conn.cursor()

    posts = inquire_new_posts(cur, LAST_RUN_DT)
    save_lastrun_datetime()
    tweet_posts(client, posts)

    cur.close()
    conn.close()
