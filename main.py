import yaml
import MySQLdb
from MySQLdb import connections, cursors
import tweepy

def load_secrets() -> dict:
    """機密情報のyamlファイルを読み込み辞書データを返す"""
    with open("secret.yaml", "r") as f:
        yaml_dict = yaml.safe_load(f.read())
    return yaml_dict

def auth_twitterAPI(API_KEY :str, API_SECRET :str, ACCESS_TOKEN :str, ACCESS_TOKEN_SECRET :str) -> tweepy.API:
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    return api

def mysql_connect(user :str, password: str, host :str, db_name :str, port :int = 3306) -> connections.Connection:
    conn = MySQLdb.connect(host=host, port=port, db=db_name, user=user, password=password)
    return conn

if __name__ == "__main__":
    SECRETS = load_secrets()
    api = auth_twitterAPI(
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
    pass