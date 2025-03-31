# Use a pipeline as a high-level helper
from transformers import pipeline
from peft import PeftModel
import torch

# pipe = pipeline("text-generation", model="hfl/chinese-llama-2-7b", framework="pt")

# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig

# base_model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-hf")
# tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-hf")
base_model = AutoModelForCausalLM.from_pretrained("hfl/chinese-llama-2-7b",device_map=None,offload_folder="E:/VSCodeProjects/ai-from-scratch/offload")
tokenizer = AutoTokenizer.from_pretrained("hfl/chinese-llama-2-7b")

lora_model = PeftModel.from_pretrained(base_model, "hfl/chinese-llama-2-lora-7b", offload_folder="E:/VSCodeProjects/ai-from-scratch/offload")   # 忽略 modules_to_save 的权重：跳过加载 embed_tokens 和 lm_head 的权重，仅加载 LoRA 参数（target_modules 的权重）

# pipe = pipeline("text-generation", model=lora_model, tokenizer=tokenizer)
# output = pipe("你好，请介绍下你自己", max_length=50)
# print(f"output:{output}")

inputs = tokenizer("你好，请介绍下你自己", return_tensors="pt").to("cuda" if torch.cuda.is_available() else "cpu")
outputs = lora_model.generate(**inputs, max_length=10)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))