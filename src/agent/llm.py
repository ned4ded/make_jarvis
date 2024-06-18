import openai

from src.config import settings


client = openai.OpenAI(api_key=settings.llm_key, base_url="https://api.theb.ai/v1")


def ask(t):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Ты помошник."},
            {"role": "user", "content": t},
        ],
    )
    return response.choices[0].message.content
