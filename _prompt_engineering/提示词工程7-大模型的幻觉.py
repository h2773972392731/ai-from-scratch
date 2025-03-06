from commonlibs import promptEngineering

prompt = f"""
给我一些研究LLM长度外推的论文，包括论文标题、主要内容和链接
"""

response = promptEngineering.get_completion(prompt)
print(response)
