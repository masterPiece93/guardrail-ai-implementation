import os
from environs import Env
from openai import AzureOpenAI

env = Env()
env.read_env()

def get_llm_client(_for: str):

    if _for.lower() == "azure":

        return AzureOpenAI(
                    api_key=env.str('AZURE_OPENAI_API_KEY'),  
                    api_version="2024-02-01",
                    azure_endpoint = env.str('AZURE_OPENAI_ENDPOINT')
                )
    
    raise NotImplementedError(f'client with name `{_for}` not found')
