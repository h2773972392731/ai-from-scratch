# 用 llama_cpp_python 运行模型

from llama_cpp import Llama

llm = Llama(model_path="C:/Users/Administrator/.cache/modelscope/hub/models/Xorbits/Qwen-7B-Chat-GGUF/Qwen-7B-Chat.Q4_K_M.gguf")
output = llm("Hello, how are you?", max_tokens=32)
print(output["choices"][0]["text"])