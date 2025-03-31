# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text-generation", model="meta-llama/Llama-2-7b-hf", framework="pt")

# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM

base_model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-hf")
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-hf")

pipe = pipeline("text-generation", model=base_model, tokenizer=tokenizer)
output = pipe("你好，请介绍下你自己", max_length=50)
print(f"output:{output}")