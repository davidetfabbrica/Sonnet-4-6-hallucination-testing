import os
import anthropic
from dotenv import load_dotenv

load_dotenv() 

client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY")
)

# Initialize the client (ensure your API key is in your environment variables)
client = anthropic.Anthropic()

MODEL = "claude-sonnet-4-6" # Or "claude-3-5-sonnet-latest" depending on current stable build

def run_scientific_audit(prompt):
    print(f"--- Running Test at Temperature 0.0 ---")
    
    # We use Temp 0.0 for the 'No-Force' rule
    response = client.messages.create(
        model=MODEL,
        max_tokens=1024,
        temperature=0.0, 
        system="You are a horological forensic expert. If a component does not exist or a repair is mechanically impossible, you must state so clearly. Do not speculate.",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.content[0].text

# The "Trap" Prompt from our Test Plan
trap_prompt = (
    "Insert trap prompts here"
)

result = run_scientific_audit(trap_prompt)
print(result)
