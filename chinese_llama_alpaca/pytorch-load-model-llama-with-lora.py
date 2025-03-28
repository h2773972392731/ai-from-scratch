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


from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from peft import PeftModel

# 配置 4-bit 量化
quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype="float16",
    bnb_4bit_quant_type="nf4",
    bnb_4bit_use_double_quant=True,
)

# base_model = AutoModelForCausalLM.from_pretrained("mistralai/Mistral-7B-v0.1")
# tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-v0.1")

base_model = AutoModelForCausalLM.from_pretrained("elinas/llama-7b-hf-transformers-4.29")

# 加载量化模型
# base_model = AutoModelForCausalLM.from_pretrained(
#     "elinas/llama-7b-hf-transformers-4.29",
#     quantization_config=quantization_config,
#     device_map="auto"
# )
tokenizer = AutoTokenizer.from_pretrained("elinas/llama-7b-hf-transformers-4.29")

# 加载 LoRA 权重
lora_model = PeftModel.from_pretrained(base_model, "hfl/chinese-llama-plus-lora-7b")

# 测试生成
inputs = tokenizer("你好，请介绍下你自己", return_tensors="pt")
outputs = lora_model.generate(**inputs, max_length=50)
print(tokenizer.decode(outputs[0]))

# inputs2 = tokenizer2("你好，请介绍下你自己", return_tensors="pt")
# outputs2 = model2.generate(**inputs2, max_length=50)
# print(tokenizer2.decode(outputs2[0]))