import openai
import os

from dotenv import load_dotenv
load_dotenv()

# APIキーを環境変数から取得する
openai.api_key = os.environ["OPENAI_API_KEY"]

# ChatGPT APIにリクエストを送信して結果を取得する
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt="Hello, how are you today?",
    max_tokens=50,
    n=1,
    stop=None,
    temperature=0.5,
)

# 結果を表示する
print(response.choices[0].text)
