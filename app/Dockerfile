# 使用するベースイメージ
FROM python:3.8

# 作業ディレクトリを設定
WORKDIR /usr/src/app

# 必要なファイルをコンテナにコピー
COPY requirements.txt ./

# 必要なパッケージをインストール
RUN pip install --no-cache-dir -r requirements.txt

# すべてのファイルを作業ディレクトリにコピー
COPY . .

# アプリケーションを実行
CMD [ "python", "./app.py" ]
