from transformers import AutoModelForCausalLM, AutoTokenizer

# 加载模型和分词器
model_name = "E:/playground/chinese-llama-lora-7b/ChineseAlpacaGroup/adapter_model.bin"  # 模型名称
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

print(model)
print(tokenizer)