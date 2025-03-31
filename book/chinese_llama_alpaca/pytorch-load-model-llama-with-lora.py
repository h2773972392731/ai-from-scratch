# Use a pipeline as a high-level helper
from transformers import pipeline


from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from peft import PeftModel
import torch

# 配置 4-bit 量化
quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype="float16",
    bnb_4bit_quant_type="nf4",
    bnb_4bit_use_double_quant=True,
)

base_model = AutoModelForCausalLM.from_pretrained(
    "elinas/llama-7b-hf-transformers-4.29"
)
tokenizer = AutoTokenizer.from_pretrained("elinas/llama-7b-hf-transformers-4.29")

# 加载量化模型
# base_model = AutoModelForCausalLM.from_pretrained(
#     "elinas/llama-7b-hf-transformers-4.29",
#     quantization_config=quantization_config,
#     device_map="auto"
# )


# 权重形状是 torch.Size([32000, 4096])，即词汇表大小为 32000
print(f"tokenizer.vocab_size:{tokenizer.vocab_size}")

# 加载 LoRA 权重
# 检查点中的 embed_tokens 和 lm_head 权重形状为 [49953, 4096]
lora_model = PeftModel.from_pretrained(
    base_model, "hfl/chinese-llama-lora-7b", ignore_mismatched_sizes=True
)  # 忽略 modules_to_save 的权重：跳过加载 embed_tokens 和 lm_head 的权重，仅加载 LoRA 参数（target_modules 的权重）

# LoRA 检查点文件（adapter_model.bin）包含 embed_tokens 和 lm_head 的权重 torch.Size([49953, 4096])
# checkpoint = torch.load("E:/models/huggingface_models/huggingface/hub/models--hfl--chinese-llama-lora-7b/snapshots/b5e520ae0a1282c6105a72ad6063a3b3de211067/adapter_model.bin", map_location="cpu")
# embed_tokens_weight = checkpoint["base_model.model.model.embed_tokens.modules_to_save.default.weight"]
# print("embed_tokens_weight.shape:"+embed_tokens_weight.shape)

# 测试生成
inputs = tokenizer("你好，请介绍下你自己", return_tensors="pt")
outputs = lora_model.generate(**inputs, max_length=50)
print(tokenizer.decode(outputs[0]))


# pipe = pipeline("text-generation", model=lora_model, tokenizer=tokenizer)
# output2 = pipe("你好，请介绍下你自己", max_length=50)
# print(output2)

# 再看：问题4，问题6
