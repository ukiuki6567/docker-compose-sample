# Docker-compose-sample

このプロジェクトは、Dockerを使用したシンプルなブログアプリケーションです。Flaskで作られたウェブアプリケーションとPostgreSQLデータベースを含んでいます。

## フォルダ構成
```
/docker-compose-sample
│  
├── app/                # Flaskアプリケーションファイルがここに格納されます  
│ ├── Dockerfile        # FlaskアプリケーションのDockerfile  
│ ├── requirements.txt  # Pythonの依存関係  
│ └── app.py            # Flaskアプリケーションのメインファイル  
│  
├── init.sql            # PostgreSQLを初期化するためのSQLスクリプト  
├── docker-compose.yml  # 複数のコンテナを管理するDocker Composeファイル  
├── .gitignore          # gitが無視すべきファイル/ディレクトリを指定  
└── README.md           # プロジェクトの説明と使用方法  
```


## 始め方

### 前提条件

- システムにDockerがインストールされている必要があります。[Dockerの公式ドキュメント](https://docs.docker.com/engine/install/ubuntu/)に従って、UbuntuにDockerをインストールしてください。

### Dockerのインストール

Dockerのインストールは、以下の手順に従って行います。詳細な手順については、[公式ドキュメント](https://docs.docker.com/engine/install/ubuntu/)を参照してください。

1. リポジトリをセットアップします。
    ```
    # Add Docker's official GPG key:
    sudo apt-get update
    sudo apt-get install ca-certificates curl gnupg
    sudo install -m 0755 -d /etc/apt/keyrings
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
    sudo chmod a+r /etc/apt/keyrings/docker.gpg

    # Add the repository to Apt sources:
    echo \
    "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
    "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
    sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    sudo apt-get update
    ```
1. Dockerエンジンをインストールします。
    ```
    sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
    ```

1. Hello Worldイメージを実行して、Dockerが正しくインストールされていることを確認します。(Option)
    ```
    sudo docker run hello-world
    ```

### アプリケーションのセットアップ

1. リポジトリをクローンします。
    ```
    git clone [あなたのリポジトリのURL]
    cd docker-compose-sample
    ```

1. Dockerイメージをビルドし、コンテナを起動します。
    ```
    sudo docker compose up --build
    ```
    アプリケーションは、指定されたポート（例：http://[ホストVMのIP]:5000）でアクセス可能です。

## 使用方法

ブラウザを開いて指定されたアドレス（デフォルトは http://[ホストVMのIP]:5000）にアクセスしてください。記事の投稿、編集、削除などが行えます。

