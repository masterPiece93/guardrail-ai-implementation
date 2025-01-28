import os
from environs import Env

env = Env()
env.read_env()


def initialize_env(_for: str):

    if _for.lower() == 'azure':

        os.environ["AZURE_API_KEY"] = env.str('AZURE_OPENAI_API_KEY')
        os.environ["AZURE_API_BASE"] = env.str('AZURE_OPENAI_ENDPOINT')
        os.environ["AZURE_API_VERSION"] = "2024-02-01"

        return
    
    raise NotImplementedError(f'Env for name `{_for}` not found')
