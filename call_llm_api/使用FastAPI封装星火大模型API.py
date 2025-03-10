# 尽管讯飞星火大模型API主要通过WebSocket进行交互，但为了满足不使用WebSocket的需求，可以通过封装本地API的方式实现。这种方法通常涉及创建一个中间层服务，该服务将HTTP请求转换为WebSocket请求，并将结果返回给客户端。下面是一个基于FastAPI的解决方案，它允许你通过标准的HTTP POST请求来调用星火大模型API。

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
from sparkai.llm.llm import ChatSparkLLM, ChunkPrintHandler
from sparkai.core.messages import ChatMessage
import os
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

app = FastAPI()

# 配置星火大模型参数
SPARKAI_URL = 'wss://spark-api.xf-yun.com/v4.0/chat'  # 替换为实际使用的版本URL
SPARKAI_APP_ID = os.environ["SPARK_APPID"]
SPARKAI_API_KEY = os.environ["SPARK_API_KEY"]
SPARKAI_API_SECRET = os.environ["SPARK_API_SECRET"]
SPARKAI_DOMAIN = '4.0Ultra'

# 初始化ChatSparkLLM
spark = ChatSparkLLM(
    spark_api_url=SPARKAI_URL,
    spark_app_id=SPARKAI_APP_ID,
    spark_api_key=SPARKAI_API_KEY,
    spark_api_secret=SPARKAI_API_SECRET,
    spark_llm_domain=SPARKAI_DOMAIN,
    streaming=False,
)

class Query(BaseModel):
    prompt: str

@app.post("/query/")
async def query_model(query: Query):
    try:
        messages = [ChatMessage(role="user", content=query.prompt)]
        handler = ChunkPrintHandler()
        response = spark.generate([messages], callbacks=[handler])
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)