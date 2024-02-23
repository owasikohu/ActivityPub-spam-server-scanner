# ActivityPub-spam-server-scanner
## 使い方
### ライブラリのインストール
``` bash
pip install aiohttp
```
### misskey.ioから接続されているサーバーを取得
``` bash
wget https://misskey.io/api/v1/instance/peers -O urls.json
```
### スクリプトを実行
``` bash
python3 scan.py
```
実行後10分程度待ってください
