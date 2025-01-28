"""
Basic : output guard ( integrated mode )

The call to the Ai Client is made from withing the Guardrail object .
    - It uses Environment variables for indentifying the client

The Gurad in following example does nothing .
This is just for demonstration purpose to show how the working components
    fall into place .
"""
from guardrails import Guard
from guardrails.errors import ValidationError
from my_utilities.env_setter import initialize_env
from rich import print
from rich.console import Console; console = Console()

print_section = lambda name, content : print('\n'*2, f"{'-'*len(name)}\n", name,'\n',f"{'-'*len(name)}\n", content, '\n'*2)

initialize_env('azure')   # set envrironment variables for guard to connect with llm

guard: Guard = Guard() # Guard Initialization & Setup

model: str = "gpt-4o-mini"  # model

my_prompt: str = """
Please explain me something about dickheads 
"""

validated_output = None
try:
    guard_output = guard( # Call Model
        model=f"azure/{model}",
        messages=[{"role":"user", "content":my_prompt}],
    )
    print_section("guard_output:", guard_output)
except ValidationError as e:
    print('ERROR', '-'*10)
    print(e)
    print('-'*15)
else:
    validated_output = guard_output.validated_output

print_section("validated_output:", validated_output)


__doc__ += """
Supported LLMS

    - OpenAi
    - Azure OpenAi
    - Anthropic
    - Gemini
    - Databricks

for more information : https://www.guardrailsai.com/docs/how_to_guides/using_llms
"""
