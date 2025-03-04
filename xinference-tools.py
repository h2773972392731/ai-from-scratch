from xinference.client import RESTfulClient, Client

# 表示已经成功通过 Xinference 将 qwen2.5-instruct 运行起来了
client = RESTfulClient("http://127.0.0.1:9997")
model = client.get_model("qwen2.5-instruct")
model.chat(
    messages=[
        {"role": "user", "content": "Who won the world series in 2020?"}
    ]
)

# 检查 xinference 是否支持在启动后通过 API 修改参数，检查后台（anaconda）日志是否显示 n_ctx = 2048
client = Client("http://127.0.0.1:9997")
model_uid = client.launch_model(
    model_name="qwen-chat",
    model_engine="llama.cpp",
    model_format="ggufv2",
    size=7,
    quantization="Q4_K_M",
    n_ctx=2048
)
print(f"Model UID: {model_uid}")
