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
        endpoint = os.environ["AZURE_MODEL_ENDPOINT"]
        key = os.environ["AZURE_INFERENCE_CREDENTIAL"]
    except KeyError:
        print("Missing environment variable 'AZURE_AI_CHAT_ENDPOINT' or 'AZURE_AI_CHAT_KEY'")
        print("Set them before running this sample.")
        exit()

    try:
        model_deployment = os.environ["AZURE_AI_CHAT_DEPLOYMENT_NAME"]
    except KeyError:
        print("Could not read optional environment variable `AZURE_AI_CHAT_DEPLOYMENT_NAME`.")
        print("HTTP request header `azureml-model-deployment` will not be set.")
        model_deployment = None

    client = ChatCompletionsClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(key),
        headers={"azureml-model-deployment": model_deployment},
    )

    response = client.complete(
        messages=[
            #SystemMessage(content="You are an AI assistant that describes images in details."),
            SystemMessage(content="You are an AI assistant that describes images in details. Think in English for Japanese questions. English answers should be translated into Japanese as your final response."),
            UserMessage(
                content=[
                    #TextContentItem(text="What's in this image?"),
                    TextContentItem(text="この画像のグラフのデータ内容を説明してください"),
                    ImageContentItem(
                        image_url=ImageUrl.load(
                            image_file="血液型.png",
                            image_format="png",
                            detail=ImageDetailLevel.HIGH,
                        ),
                    ),
                ],
            ),
        ],
    )

    print(response.choices[0].message.content)


if __name__ == "__main__":
    sample_chat_completions_with_image_data()