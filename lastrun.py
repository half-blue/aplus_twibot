import datetime

import yaml

"""
実行時にlastrun.yamlを読み込み、このプログラムがいつ最後に実行されたかを知る

実行修了時に現在時刻を書き込む

時刻はすべてUTCでやり取りする。djangoはDBにUTCで時刻を書き込むため。
"""

def load_lastrun_datetime() -> str:
    """最終実行時刻(UTC)を読みだす"""
    with open("lastrun.yaml", "r") as f:
        yaml_dict = yaml.safe_load(f.read())
    return yaml_dict["LastRunDateTime"]

def save_lastrun_datetime() -> None:
    """現在時刻を最終実行時刻(UTC)として書き出す"""
    dt = datetime.datetime.now(datetime.timezone.utc)
    yaml_dict = {
        "LastRunDateTime" : str(dt)
    }
    with open("lastrun.yaml", "w") as f:
        yaml.dump(yaml_dict, f)