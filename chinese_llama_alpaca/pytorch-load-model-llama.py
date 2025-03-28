# from transformers import AutoModelForCausalLM, AutoTokenizer
# from peft import PeftModel

# # 加载基础模型
# base_model = AutoModelForCausalLM.from_pretrained("mistralai/Mistral-7B-v0.1")
# tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-v0.1")

# # 加载 LoRA 权重
# model = PeftModel.from_pretrained(base_model, "JingzeShi/Mixtral-7B-v0.1")

# inputs = tokenizer("你好，你是谁？", return_tensors="pt")
# outputs = model.generate(**inputs, max_length=50)
# print(tokenizer.decode(outputs[0]))


from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("elinas/llama-7b-hf-transformers-4.29")
tokenizer = AutoTokenizer.from_pretrained("elinas/llama-7b-hf-transformers-4.29")

inputs = tokenizer("你好，请介绍下你自己", return_tensors="pt")
outputs = model.generate(**inputs, max_length=50)
print(tokenizer.decode(outputs[0]))