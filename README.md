# aplus_twibot
A+つくばに新規投稿された質問をツイートするBOTシステム

## 使用法
#### ライブラリの追加
```sh
pip3 install pyyaml
pip3 install tweepy
```
#### リポジトリのクローン
```sh
git clone -b main --depth 1 https://github.com/half-blue/aplus_twibot.git
```
#### 機密情報の設定
`secret_origin.yaml`を編集し、`secret.yaml`として保存してください。

#### 最終実行時刻の初期設定
このBOTは`lastrun.yaml`に書き込まれた最終実行時刻(UTC)を参照し、最終実行時刻以降に投稿された質問をツイートします。
そのため、必ず適切な初期最終実行時刻を与える必要があります。

`lastrun.py`に最終実行時刻を書き込む関数があるため、それを利用し初期ファイルを生成します。
```sh
python3 -c "import lastrun; lastrun.save_lastrun_datetime()"
cat lastrun.yaml
```

#### 実行
 ```
 python3 main.py
 ```
 
## 自動実行の設定
cronで5分おきに自動実行されます。

 `/etc/cron.d/twitter_bot`に自動実行の設定が記述されています。
 ```
 */5 * * * * root /usr/bin/python3 /home/django/aplus_twibot/main.py >> /var/log/twibot.log 2>> /var/log/twibot_error.log
 ```
 標準出力と標準エラー出力はご覧のようにリダイレクションされます。

## 留意事項
エラー処理を全くしていません。質問数が増えるとおかしくなると思います。その場合はこのBOTを止めてください。
