import openai
import os
import textwrap

from dotenv import load_dotenv
load_dotenv()

# APIキーを環境変数から取得する
openai.api_key = os.environ["OPENAI_API_KEY"]

# テスト用
# with open("./data/test.txt", "r", encoding="utf-8") as f:
#   words = [word for word in f.read().splitlines()]

with open("./data/input.txt", "r", encoding="utf-8") as f:
  words = [word for word in f.read().splitlines()]


# ChatGPT APIにリクエストを送信して結果を取得する
for word in words:
  prompt = f'''
    {word}はネットワーク用語です。
    {word}について2048文字程度のWikipedia風解説記事をMarkdownで書いてください。
    構成は、対象の用語と正称を見出し1、その後に「特徴」・「応用例」・「注意点」・「関連用語」をそれぞれ見出し2のセクションに分けて書いてください。特徴を丁寧に書いてください。
    また、セクションごとに空行を開けて、見出し1は#、見出し2は##で書いてください。また、文字は左寄せで書いてください。指定したセクション以外の見出しはつけないでください。
  '''

  response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=textwrap.dedent(prompt)[1:-1],
      max_tokens=2048,
      n=1,
      stop=None,
      temperature=0.5,
      frequency_penalty=0.5,
      presence_penalty=0.5,
  )

  result = response.choices[0].text

  print(result, end="\n\n")

  # 変数にファイルパスが含まれる場合変換する
  word = word.replace("/", "_")

  # 生成された記事をファイルに保存する
  with open(f"./output/{word}.md", "w") as f:
    f.write(result)
