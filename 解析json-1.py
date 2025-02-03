import json

# 假设这是你的JSON字符串
json_str = '[{"pid":3,"pname":"颜色","vid":10061,"vname":"黑色"},{"pid":802,"pname":"规格","vid":-2,"vname":"40码"}]'

# 将字符串解析为Python列表
data = json.loads(json_str)

print(type(data))

print(data[1]['vname'])
