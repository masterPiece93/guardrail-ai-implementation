"""
This Script is using : `AzureOpenAI` client
"""
import os
from environs import Env
from openai import AzureOpenAI

env = Env()
env.read_env()

os.environ["AZURE_OPENAI_API_KEY"] = env.str('AZURE_OPENAI_API_KEY')
os.environ["AZURE_OPENAI_ENDPOINT"] = env.str('AZURE_OPENAI_ENDPOINT')

client = AzureOpenAI(api_version="2024-02-01")

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
)

print(completion.choices[0].message)