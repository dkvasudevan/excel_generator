from openai import OpenAI
client = OpenAI()


def create_completion(prompt: str) -> str:
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an expert at microsoft excel and have 30 years of industry experience with excel."},
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message.content