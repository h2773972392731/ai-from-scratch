import sys

sys.path.append("../../commonlibs")  # 将父目录放入系统路径中

# 使用智谱 Embedding API，注意，需要将上一章实现的封装代码下载到本地
from commonlibs.zhipuai_embedding import ZhipuAIEmbeddings

from langchain.vectorstores.chroma import Chroma
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv, find_dotenv
import os

_ = load_dotenv(find_dotenv())  # read local .env file
zhipuai_api_key = os.environ['ZHIPUAI_API_KEY']
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

# 定义 Embeddings
embedding = ZhipuAIEmbeddings()

# 向量数据库持久化路径
persist_directory = '../../data_base/vector_db/chroma'

# 加载数据库
vectordb = Chroma(
    persist_directory=persist_directory,  # 允许我们将persist_directory目录保存到磁盘上
    embedding_function=embedding
)

# 使用 OpenAI GPT-3.5 模型
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA

# A prompt（简明扼要）
template_v1 = """使用以下上下文来回答最后的问题。如果你不知道答案，就说你不知道，不要试图编造答
案。最多使用三句话。尽量使答案简明扼要。总是在回答的最后说“谢谢你的提问！”。
{context}
问题: {question}
"""

QA_CHAIN_PROMPT = PromptTemplate(input_variables=["context", "question"],
                                 template=template_v1)

qa_chain = RetrievalQA.from_chain_type(llm,
                                       retriever=vectordb.as_retriever(),
                                       return_source_documents=True,
                                       chain_type_kwargs={"prompt": QA_CHAIN_PROMPT})

print("问题一：")
question = "南瓜书和西瓜书有什么关系？"
result = qa_chain({"query": question})
print(result["result"])

print("问题二：")
question = "应该如何使用南瓜书？"
result = qa_chain({"query": question})
print(result["result"])

# B prompt（简明扼要）
template_v2 = """使用以下上下文来回答最后的问题。如果你不知道答案，就说你不知道，不要试图编造答
案。你应该使答案尽可能详细具体，但不要偏题。如果答案比较长，请酌情进行分段，以提高答案的阅读体验。
{context}
问题: {question}
有用的回答:"""

QA_CHAIN_PROMPT = PromptTemplate(input_variables=["context", "question"],
                                 template=template_v2)

qa_chain = RetrievalQA.from_chain_type(llm,
                                       retriever=vectordb.as_retriever(),
                                       return_source_documents=True,
                                       chain_type_kwargs={"prompt": QA_CHAIN_PROMPT})

print("问题一：")
question = "南瓜书和西瓜书有什么关系？"
result = qa_chain({"query": question})
print(result["result"])

print("问题二：")
question = "应该如何使用南瓜书？"
result = qa_chain({"query": question})
print(result["result"])
