from zhipuai import ZhipuAI
import os
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

def zhipu_embedding(text: str):
    api_key = os.environ['ZHIPUAI_API_KEY']
    client = ZhipuAI(api_key=api_key)
    response = client.embeddings.create(
        model="embedding-2",
        input=text,
    )
    return response


text = '要生成 embedding 的输入文本，字符串形式。'
response = zhipu_embedding(text=text)

# response为zhipuai.types.embeddings.EmbeddingsResponded类型，我们可以调用object、data、model、usage来查看response的embedding类型、embedding、embedding model及使用情况。
print(f'response类型为：{type(response)}')
print(f'embedding类型为：{response.object}')
print(f'生成embedding的model为：{response.model}')
print(f'生成的embedding长度为：{len(response.data[0].embedding)}')
print(f'embedding（前10）为: {response.data[0].embedding[:10]}')
