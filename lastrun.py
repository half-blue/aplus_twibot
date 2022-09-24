import datetime

import yaml

"""
実行時にlastrun.yamlを読み込み、このプログラムがいつ最後に実行されたかを知る

実行修了時に現在時刻を書き込む
"""

def load_lastrun_datetime() -> str:
    """最終実行時刻を読みだす"""
    with open("lastrun.yaml", "r") as f:
        yaml_dict = yaml.safe_load(f.read())
    return yaml_dict["LastRunDateTime"]

def save_lastrun_datetime() -> None:
    """現在時刻を最終実行時刻として書き出す"""
    dt = datetime.datetime.now()
    yaml_dict = {
        "LastRunDateTime" : str(dt)
    }
    with open("lastrun.yaml", "w") as f:
        yaml.dump(yaml_dict, f)