from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel

# 加载原始 LLaMA 模型（需要申请访问权限）
base_model = AutoModelForCausalLM.from_pretrained("meta-llama/LLaMA-2-7b")
tokenizer = AutoTokenizer.from_pretrained("meta-llama/LLaMA-2-7b")

# 加载 Chinese-LLaMA-7B 的 LoRA 权重
model = PeftModel.from_pretrained(base_model, "hfl/chinese-llama-7b")

# 测试生成
inputs = tokenizer("你好，你是谁？", return_tensors="pt")
outputs = model.generate(**inputs, max_length=50)
print(tokenizer.decode(outputs[0]))