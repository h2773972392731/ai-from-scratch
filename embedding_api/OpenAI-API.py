# text-embedding-3-large有最好的性能和最贵的价格，当我们搭建的应用需要更好的表现且成本充足的情况下可以使用；
# text-embedding-3-small有着较好的性能跟价格，当我们预算有限时可以选择该模型；
# 而text-embedding-ada-002是OpenAI上一代的模型，无论在性能还是价格都不如及前两者，因此不推荐使用。

import os
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

# 读取本地/项目的环境变量。
# find_dotenv()寻找并定位.env文件的路径
# load_dotenv()读取该.env文件，并将其中的环境变量加载到当前的运行环境中
# 如果你设置的是全局的环境变量，这行代码则没有任何作用。
_ = load_dotenv(find_dotenv())


# 如果你需要通过代理端口访问，你需要如下配置
# os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:7890'
# os.environ["HTTP_PROXY"] = 'http://127.0.0.1:7890'

def openai_embedding(text: str, model: str = None):
    # 获取环境变量 OPENAI_API_KEY
    api_key = os.environ['OPENAI_API_KEY']
    client = OpenAI(api_key=api_key)

    # embedding model：'text-embedding-3-small', 'text-embedding-3-large', 'text-embedding-ada-002'
    if model == None:
        model = "text-embedding-3-small"

    response = client.embeddings.create(
        input=text,
        model=model
    )
    return response


response = openai_embedding(text='要生成 embedding 的输入文本，字符串形式。')

# 返回的embedding类型为：list
print(f'返回的embedding类型为：{response.object}')

# embedding长度为：1536
print(f'embedding长度为：{len(response.data[0].embedding)}')

# embedding（前10）为：[0.03884002938866615, 0.013516489416360855, -0.0024250170681625605, -0.01655769906938076, 0.024130908772349358, -0.017382603138685226, 0.04206013306975365, 0.011498954147100449, -0.028245486319065094, -0.00674333656206727]
print(f'embedding（前10）为：{response.data[0].embedding[:10]}')

# 本次embedding model为：text-embedding-3-small
print(f'本次embedding model为：{response.model}')

# 本次token使用情况为：Usage(prompt_tokens=12, total_tokens=12)
print(f'本次token使用情况为：{response.usage}')

# API返回的数据为json格式，除object向量类型外还有存放数据的data、embedding model 型号model以及本次 token 使用情况usage等数据，具体如下所示：
#
# {
#   "object": "list",
#   "data": [
#     {
#       "object": "embedding",
#       "index": 0,
#       "embedding": [
#         -0.006929283495992422,
#         ... (省略)
#         -4.547132266452536e-05,
#       ],
#     }
#   ],
#   "model": "text-embedding-3-small",
#   "usage": {
#     "prompt_tokens": 5,
#     "total_tokens": 5
#   }
# }
