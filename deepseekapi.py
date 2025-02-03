from openai import OpenAI

client = OpenAI(api_key="sk-24db43d0275145c3bdc406f6d1d9fdd7", base_url="https://api.deepseek.com/v1")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
    ],
    stream=False
)

print('...')
print(response.choices[0].message.content)