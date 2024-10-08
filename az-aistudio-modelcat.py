"""
このスクリプトは、Azure AI Inference APIを使用してチャットコンプリートのリクエストを送信し、回答を取得する方法を示しています。

主なステップ:
1. .envファイルから環境変数を読み込む。
2. 環境変数からAzure Inference APIの認証キーを取得する。
3. ChatCompletionsClientを初期化する。
4. モデル情報を取得し、モデル名、モデルタイプ、モデル提供者名を表示する。
5. チャットコンプリートのリクエストを作成し、APIに送信する。
6. レスポンスの内容、使用されたトークン数を表示する。

使用されるライブラリ:
- os: 環境変数を操作するために使用。
- azure.ai.inference: Azure AI推論APIクライアント。
- azure.core.credentials: Azureの認証情報を管理するために使用。
- dotenv: .envファイルから環境変数を読み込むために使用。
"""
# pip install azure-ai-inference
import os
from azure.ai.inference import ChatCompletionsClient
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("AZURE_INFERENCE_CREDENTIAL", '')
if not api_key:
  raise Exception("A key should be provided to invoke the endpoint")

client = ChatCompletionsClient(
    endpoint=os.getenv("AZURE_MODEL_ENDPOINT", ''),
    credential=AzureKeyCredential(api_key)
)

model_info = client.get_model_info()
print("Model name:", model_info.model_name)
print("Model type:", model_info.model_type)
print("Model provider name:", model_info.model_provider_name)

payload = {
  "messages": [
    {
      "role": "user",
      "content": "I am going to Paris, what should I see?"
    },
    {
      "role": "assistant",
      "content": "Paris, the capital of France, is known for its stunning architecture, art museums, historical landmarks, and romantic atmosphere. Here are some of the top attractions to see in Paris:\n\n1. The Eiffel Tower: The iconic Eiffel Tower is one of the most recognizable landmarks in the world and offers breathtaking views of the city.\n2. The Louvre Museum: The Louvre is one of the world's largest and most famous museums, housing an impressive collection of art and artifacts, including the Mona Lisa.\n3. Notre-Dame Cathedral: This beautiful cathedral is one of the most famous landmarks in Paris and is known for its Gothic architecture and stunning stained glass windows.\n\nThese are just a few of the many attractions that Paris has to offer. With so much to see and do, it's no wonder that Paris is one of the most popular tourist destinations in the world."
    },
    {
      "role": "user",
      "content": "What is so great about #1?"
    }
  ],
  "max_tokens": 2048,
  "temperature": 0,
  "top_p": 1
}
response = client.complete(payload)

print("Response:", response.choices[0].message.content)
print("Model:", response.model)
print("Usage:")
print("	Prompt tokens:", response.usage.prompt_tokens)
print("	Total tokens:", response.usage.total_tokens)
print("	Completion tokens:", response.usage.completion_tokens)
