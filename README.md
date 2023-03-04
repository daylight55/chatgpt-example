# ChatGPT Example

ネットワークスペシャリストの用語解説記事をMarkdownで出力します。
また、作成後はHugoでビルドしたページをGithub Actionsを使いGithub Pagesにホスティングします。



ネットワークスペシャリストの語句一覧はこちらの記事の略称一覧を使用させて頂きました。  
[令和元(2019)年ネットワークスペシャリスト試験略号一覧 - Qiita](https://qiita.com/kaizen_nagoya/items/24c7f2ea3fe0b4ce434b)

## Recommended
- asdf
- python 
- poetry
- hugo

Please refer to `.tool-versions` for the version

## Try

Setup
```
git clone git@github.com:daylight55/chatgpt-example.git
cd chatgpt-example
poetry install
```

Sets API key
```
cp .env.sample .env
# Set .env
vi .env
```

Run
```
poetry shell
.venv ❯ python main.py
```

## Viewer

```
hugo server
```
