"""
Basic : input guard

The Gurad in following example does nothing .
This is just for demonstration purpose to show how the working components
    fall into place .
"""
from guardrails import Guard
from rich import print
from rich.console import Console; console = Console()

guard = Guard()

result = guard.parse("This is some input text/prompt from user that is to be guraded")

print(result)
print("validation_passed : ", result.validation_passed)
print("validated_output : ", result.validated_output)

# now the validated output can be passed on to the llm for processing .
