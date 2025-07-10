from openai import OpenAI
from config.prompts import prompts
import json


def initialize_client():
    with open("config/openai_key.json", "r") as f:
        api_key = json.load(f)["api_key"]
    return OpenAI(api_key=api_key)

client = initialize_client()

def load_prompt(key):
    return prompts.get(key, "")

def generate_text(prompt):
    messages = [{"role": "user", "content" : prompt}]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=500,
        temperature=0.1,
        top_p=1.0
    )
    return response.choices[0].message.content.strip()