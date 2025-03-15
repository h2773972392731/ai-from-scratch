import requests
import json
import os

# API 密钥（替换为你的实际密钥）
API_KEY = os.environ["GEMINI_API_KEY"]

# API 端点 URL
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

# 请求头
headers = {
    "Content-Type": "application/json"
}

# 请求体（与 curl 中的 -d 参数对应）
payload = {
    "contents": [{
        "parts": [{"text": "Explain how AI works"}]
    }]
}

# 发送 POST 请求
response = requests.post(url, headers=headers, data=json.dumps(payload))

# 检查响应状态并输出结果
if response.status_code == 200:
    print("成功获取响应：")
    print(response.json())  # 打印返回的 JSON 数据
else:
    print(f"请求失败，状态码：{response.status_code}")
    print(response.text)  # 打印错误信息