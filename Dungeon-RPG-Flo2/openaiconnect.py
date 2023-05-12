import openai
from dotenv import load_dotenv
import os

#Before loading: Create a .env with your API KEY and add to .gitignore
load_dotenv()

GPT_KEY_PTITLU = os.getenv('GPT_KEY_PTITLU')
# print (GPT_KEY_PTITLU)

openai.api_key = GPT_KEY_PTITLU

while True:
    prompt = input("Prompt:")

    response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=1000,
    n=1,
    stop=None,
    temperature=0.5,
    )
    
    response = response.choices[0].text.strip()
    print(response)
