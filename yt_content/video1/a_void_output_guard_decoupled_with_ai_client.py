"""
Basic : output guard ( decoupled method )

The call to the ai client is made first , and then we pass the
    output to the guardrail .

The Gurad in following example does nothing .
This is just for demonstration purpose to show how the working components
    fall into place .
"""
from guardrails import Guard
from guardrails.errors import ValidationError
from my_utilities.llm_client import get_llm_client
from rich import print
from rich.console import Console; console = Console()

print_section = lambda name, content : print('\n'*2, f"{'-'*len(name)}\n", name,'\n',f"{'-'*len(name)}\n", content, '\n'*2)

client = get_llm_client('azure')    # create llm client object 

guard: Guard = Guard()  # Guard Initialization & Setup

model = 'gpt-4o-mini'   # model

my_prompt: str = """
Please explain me something about dickheads 
"""

response = client.completions.create(
        model=model, 
        prompt=my_prompt, 
        max_tokens=100
    )

llm_response_text: str = response.choices[0].text

print_section("llm_response_text:", llm_response_text)

validated_output = None
try:
    guard_output = guard.parse(
        llm_output=llm_response_text
    )
    print_section("guard_output:", guard_output)
except ValidationError as e:
    print('ERROR', '-'*10)
    print(e)
    print('-'*15)
else:
    validated_output = guard_output.validated_output

print_section("validated_output:", validated_output)

