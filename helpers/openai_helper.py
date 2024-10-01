from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI()
client.api_key= os.getenv("OPENAI_API_KEY")

def create_completion(prompt: str) -> str:
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an expert at microsoft excel and have 30 years of industry experience with excel."},
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message.content