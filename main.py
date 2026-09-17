from pathlib import Path

import dotenv
from openai import OpenAI

# Load api key
dotenv.load_dotenv()

# Load client
client = OpenAI()

prompt = """

You are a document information extraction system.

Analyze the provided document and extract:

1. document type
2. date
3. people mentioned
4. action items
5. deadlines
6. a short summary

Rules:
- Do not invent information.
- If information is missing, return null.
- Preserve dates when explicitly provided.
- Separate each action item.
- Return structured JSON.

"""

file = "meeting.txt"
file_path = Path(f"documents/{file}")
filename = file_path.stem

# Get document
document = open(f'documents/{file}').read()

response = client.responses.create(
    model='gpt-5.5',
    instructions=prompt,
    input=document,
)

output = response.output_text

# Save
with open(f'output/{filename}_extracted.json', 'w') as f:
    f.write(output)

print("File saved successfully")


