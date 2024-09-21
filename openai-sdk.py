"""
このスクリプトは、OpenAIのAPIを使用してチャットコンプリートのリクエストを送信する方法を示しています。

主なステップ:
1. .envファイルから環境変数を読み込む。
2. 環境変数からGitHubトークンを取得する。
3. OpenAI APIのエンドポイントとモデル名を設定する。
4. OpenAIクライアントを初期化する。
5. チャットコンプリートのリクエストを作成し、APIに送信する。

使用されるライブラリ:
- os: 環境変数を操作するために使用。
- openai: OpenAI APIクライアント。
- dotenv: .envファイルから環境変数を読み込むために使用。
"""
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "gpt-4o"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content": "What is the capital of France?",
        }
    ],
    temperature=1.0,
    top_p=1.0,
    max_tokens=1000,
    model=model_name
)

print(response.choices[0].message.content)