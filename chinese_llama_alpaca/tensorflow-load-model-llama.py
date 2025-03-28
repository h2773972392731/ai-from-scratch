from transformers import TFLLaMAForCausalLM, AutoTokenizer
import tensorflow as tf

model = TFLLaMAForCausalLM.from_pretrained("meta-llama/LLaMA-2-7b")
tokenizer = AutoTokenizer.from_pretrained("meta-llama/LLaMA-2-7b")

inputs = tokenizer("Hello, how are you?", return_tensors="tf")
outputs = model.generate(**inputs)
print(tokenizer.decode(outputs[0]))