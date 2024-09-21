"""
このスクリプトは、AzureAI ModelInference APIを使用してチャットコンプリートのリクエストを送信する方法を示しています。

主なステップ:
1. .envファイルから環境変数を読み込む。
2. 環境変数からGitHubトークンを取得する。
3. AzureAI ModelInference APIのエンドポイントとモデル名を設定する。
4. ChatCompletionsClientを初期化する。
5. チャットコンプリートのリクエストを作成し、APIに送信する。

使用されるライブラリ:
- os: 環境変数を操作するために使用。
- azure.ai.inference: Azure AI推論APIクライアント。
- azure.core.credentials: Azureの認証情報を管理するために使用。
- dotenv: .envファイルから環境変数を読み込むために使用。
"""
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv

load_dotenv()

endpoint = "https://models.inference.ai.azure.com"
model_name = os.environ["MODEL_NAME"]
token = os.environ["GITHUB_TOKEN"]

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = client.complete(
    messages=[
        SystemMessage(content="You are a helpful assistant."),
        UserMessage(content="What is the capital of Japan?"),
    ],
    temperature=1.0,
    top_p=1.0,
    max_tokens=1000,
    model=model_name
)

print(response.choices[0].message.content)