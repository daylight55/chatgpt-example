import openai
import os

from dotenv import load_dotenv
load_dotenv()

# APIキーを環境変数から取得する
openai.api_key = os.environ["OPENAI_API_KEY"]

with open("./data/input.txt", "r", encoding="utf-8") as f:
    words = f.readlines()

# ChatGPT APIにリクエストを送信して結果を取得する
for word in words:
  response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=f"{word}はネットワーク用語です。{word}について2048文字程度のブログ風解説記事をMarkdownで、特徴・応用例・ネットワークスペシャリスト試験における注意点のセクションに分けて書いてください。",
      max_tokens=2048,
      n=1,
      stop=None,
      temperature=0.5,
      frequency_penalty=0.5,
      presence_penalty=0.5,
  )

  result = response.choices[0].text

  print(result)

  # 生成された記事をファイルに保存する
  with open(f"./output/{word}.md", "w") as f:
      f.write(result)
