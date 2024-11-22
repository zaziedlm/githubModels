# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
"""
DESCRIPTION:
    This sample demonstrates how to get a chat completions response from
    the service using a synchronous client. The sample shows how to load
    an image from a file and include it in the input chat messages.
    This sample will only work on AI models that support image input.
    Only these AI models accept the array form of `content` in the
    `UserMessage`, as shown here.

    This sample assumes the AI model is hosted on a Serverless API or
    Managed Compute endpoint. For GitHub Models or Azure OpenAI endpoints,
    the client constructor needs to be modified. See package documentation:
    https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/ai/azure-ai-inference/README.md#key-concepts

USAGE:
    python sample_chat_completions_with_image_data.py

    Set these two or three environment variables before running the sample:
    1) AZURE_AI_CHAT_ENDPOINT - Your endpoint URL, in the form 
        https://<your-deployment-name>.<your-azure-region>.models.ai.azure.com
        where `your-deployment-name` is your unique AI Model deployment name, and
        `your-azure-region` is the Azure region where your model is deployed.
    2) AZURE_AI_CHAT_KEY - Your model key (a 32-character string). Keep it secret.
    3) AZURE_AI_CHAT_DEPLOYMENT_NAME - Optional. The value for the HTTP
        request header `azureml-model-deployment`.
"""
from dotenv import load_dotenv

load_dotenv()

def sample_chat_completions_with_image_data():
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import (
        SystemMessage,
        UserMessage,
        TextContentItem,
        ImageContentItem,
        ImageUrl,
        ImageDetailLevel,
    )
    from azure.core.credentials import AzureKeyCredential

    try:
        endpoint = os.environ["AZ-TSUZUMI_ENDPOINT"]
        key = os.environ["AZ-TSUZUMI_INFERENCE_CREDENTIAL"]
    except KeyError:
        print("Missing environment variable 'AZURE_AI_CHAT_ENDPOINT' or 'AZURE_AI_CHAT_KEY'")
        print("Set them before running this sample.")
        exit()

    client = ChatCompletionsClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(key),
    )

    model_info = client.get_model_info()
    print("Model name:", model_info.model_name)
    print("Model type:", model_info.model_type)
    print("Model provider name:", model_info.model_provider_name)

    payload = {
        "messages": [
            {
            "role": "user",
            "content": "東京に行く予定ですが、何を見ればいいですか？"
            },
            {
            "role": "assistant",
            "content": "東京は、日本の首都であり、現代的な都市景観と伝統的な文化が共存する魅力的な都市です。以下は東京で訪れるべきおすすめスポットです：\n\n1. 東京タワー: 東京の象徴的なランドマークで、展望台からは素晴らしい景色が楽しめます。\n2. 浅草と浅草寺: 江戸時代から続く歴史あるエリアで、日本の伝統的な雰囲気が感じられます。\n3. 渋谷スクランブル交差点: 世界的に有名な交差点で、東京の活気を体験できます。\n\nこれらは東京が提供する多くの魅力の一部です。他にもたくさんの観光スポットがありますので、ぜひ東京を満喫してください。"
            },
            {
            "role": "user",
            "content": "大阪はどうですか？"
            }
        ],
        "max_tokens": 4096,
        "temperature": 0.15
    }
    response = client.complete(payload)

    print("Response:", response.choices[0].message.content)
    print("Model:", response.model)
    print("Usage:")
    print("	Prompt tokens:", response.usage.prompt_tokens)
    print("	Total tokens:", response.usage.total_tokens)
    print("	Completion tokens:", response.usage.completion_tokens)


if __name__ == "__main__":
    sample_chat_completions_with_image_data()