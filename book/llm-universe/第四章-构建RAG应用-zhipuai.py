# import sys
# sys.path.append("../C3 搭建知识库")  # 将父目录放入系统路径中

# 使用智谱 Embedding API，注意，需要将上一章实现的封装代码下载到本地
from commonlibs.zhipuai_embedding import ZhipuAIEmbeddings

from langchain_community.vectorstores import Chroma
from langchain_chroma import Chroma

from dotenv import load_dotenv, find_dotenv
import os
from langchain_core.messages import AIMessage
from langchain_openai import ChatOpenAI
from zhipuai import ZhipuAI

# 1. 加载向量数据库
_ = load_dotenv(find_dotenv())  # read local .env file
zhipuai_api_key = os.environ['ZHIPUAI_API_KEY']

# 加载向量数据库，其中包含了 ./data_base/knowledge_db 下多个文档的 Embedding
# 定义 Embeddings
embedding = ZhipuAIEmbeddings()

# 向量数据库持久化路径
persist_directory = './data_base/vector_db/chroma'

# 加载数据库
vectordb = Chroma(
    persist_directory=persist_directory,  # 允许我们将persist_directory目录保存到磁盘上
    embedding_function=embedding
)

print(f"向量库中存储的数量：{vectordb._collection.count()}")

# 我们可以测试一下加载的向量数据库，使用一个问题 query 进行向量检索。如下代码会在向量数据库中根据相似性进行检索，返回前 k 个最相似的文档。
# 使用相似性搜索前，请确保你已安装了 OpenAI 开源的快速分词工具 tiktoken 包：pip install tiktoken

question = "什么是prompt engineering?"
docs = vectordb.similarity_search(question, k=3)
print(f"检索到的内容数：{len(docs)}")

# 打印一下检索到的内容
for i, doc in enumerate(docs):
    print(f"检索到的第{i}个内容: \n {doc.page_content}",
          end="\n-----------------------------------------------------\n")

# 检索到的第0个内容: ...
# 检索到的第1个内容: ...
# 检索到的第2个内容: ...


# 2. 创建一个 LLM
# OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

api_key = os.environ["ZHIPUAI_API_KEY"]

# get_completion("你好")
from commonlibs.zhipuai_llm import ZhipuAILLM

# llm = ZhipuAILLM(temperature=0.1, api_key=api_key)
llm = ZhipuAILLM()
print(f"llm: {llm}")

llm.invoke("请你自我介绍一下自己！")

AIMessage(
    content='你好，我是一个智能助手，专门为用户提供各种服务和帮助。我可以回答问题、提供信息、解决问题等等。如果您有任何需要，请随时告诉我，我会尽力帮助您的。感谢您的使用！',
    response_metadata={'token_usage': {'completion_tokens': 81, 'prompt_tokens': 20, 'total_tokens': 101},
                       'model_name': 'glm-4-plus', 'system_fingerprint': 'fp_3bc1b5746c', 'finish_reason': 'stop',
                       'logprobs': None})

from langchain.prompts import PromptTemplate

# 3. 构建检索问答链
template = """使用以下上下文来回答最后的问题。如果你不知道答案，就说你不知道，不要试图编造答
案。最多使用三句话。尽量使答案简明扼要。总是在回答的最后说“谢谢你的提问！”。
{context}
问题: {question}
"""

QA_CHAIN_PROMPT = PromptTemplate(input_variables=["context", "question"],
                                 template=template)

from langchain.chains import RetrievalQA

# 再创建一个基于模板的检索链：

qa_chain = RetrievalQA.from_chain_type(llm,
                                       retriever=vectordb.as_retriever(),
                                       return_source_documents=True,
                                       chain_type_kwargs={"prompt": QA_CHAIN_PROMPT})

# 创建检索 QA 链的方法 RetrievalQA.from_chain_type() 有如下参数：
# llm：指定使用的 LLM
# 指定 chain type : RetrievalQA.from_chain_type(chain_type="map_reduce")，也可以利用load_qa_chain()方法指定chain type。
# 自定义 prompt ：通过在RetrievalQA.from_chain_type()方法中，指定chain_type_kwargs参数，而该参数：chain_type_kwargs = {"prompt": PROMPT}
# 返回源文档：通过RetrievalQA.from_chain_type()方法中指定：return_source_documents=True参数；也可以使用RetrievalQAWithSourceChain()方法，返回源文档的引用（坐标或者叫主键、索引）

# 4.检索问答链效果测试
question_1 = "什么是南瓜书？"
question_2 = "王阳明是谁？"

# 4.1 基于召回结果和 query 结合起来构建的 prompt 效果
result = qa_chain({"query": question_1})
print("大模型+知识库后回答 question_1 的结果：")
print(result["result"])

result = qa_chain({"query": question_2})
print("大模型+知识库后回答 question_2 的结果：")
print(result["result"])

# 4.2 大模型自己回答的效果
prompt_template = """请回答下列问题:
                            {}""".format(question_1)

### 基于大模型的问答
llm.predict(prompt_template)

prompt_template = """请回答下列问题:
                            {}""".format(question_2)

### 基于大模型的问答
llm.predict(prompt_template)

# 通过以上两个问题，我们发现 LLM 对于一些近几年的知识以及非常识性的专业问题，回答的并不是很好。而加上我们的本地知识，就可以帮助 LLM 做出更好的回答。另外，也有助于缓解大模型的“幻觉”问题。
