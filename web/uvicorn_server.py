# 在命令行中执行以下命令：
# uvicorn uvicorn_server:app --reload
# uvicorn uvicorn_server:app --host 127.0.0.1 --port 8000
# 这将启动一个名为 main 的 ASGI 应用程序，使用 Uvicorn 服务器运行在本地主机的默认端口 8000 上，并监听根路径 / 的 GET 请求。在浏览器中访问 http://localhost:8000，将看到 "Hello, World!" 的消息。

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}