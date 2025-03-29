from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("elinas/llama-7b-hf-transformers-4.29")
tokenizer = AutoTokenizer.from_pretrained("elinas/llama-7b-hf-transformers-4.29")

# 权重形状是 torch.Size([32000, 4096])，即词汇表大小为 32000
print(tokenizer.vocab_size)

inputs = tokenizer("你好，请介绍下你自己", return_tensors="pt")
outputs = model.generate(**inputs, max_length=50)
print(tokenizer.decode(outputs[0]))