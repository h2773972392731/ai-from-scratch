# 用 llama_cpp_python运行模型，llama_cpp_python底层调用的是llama.cpp，llama.cpp是推理引擎，是可以加载模型的，因此llama_cpp_python可以运行模型

from llama_cpp import Llama

# company
llm = Llama(
    # company
    model_path="C:/Users/2000101497/.cache/modelscope/hub/models/Xorbits/Qwen-7B-Chat-GGUF/Qwen-7B-Chat.Q4_K_M.gguf"
    # home
    # model_path="C:/Users/Administrator/.cache/modelscope/hub/models/Xorbits/Qwen-7B-Chat-GGUF/Qwen-7B-Chat.Q4_K_M.gguf"
)
output = llm("Hello, how are you?", max_tokens=32)
print(output["choices"][0]["text"])
