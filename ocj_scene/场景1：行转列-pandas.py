import pandas as pd
import json

# pandas 是最常用且高效的解决方案，尤其是当你需要处理大型数据集时。
# openpyxl 提供了更多控制Excel格式的能力，适合需要细致控制的场景。
# numpy 更适用于数学计算密集型任务，但同样可以高效地处理数据转置。
# xlrd + xlwt 适用于老版本的Excel文件，但不再推荐用于现代的 .xlsx 文件。

# 假设这是你的JSON字符串
# json_str = '[{"pid":3,"pname":"颜色","vid":10061,"vname":"黑色"},{"pid":802,"pname":"规格","vid":-2,"vname":"40码"}]'

pd.options.display.max_columns = 999

df = pd.read_excel('xlsx/ods_ic_item_sku_17218746.xlsx')



df['sku_code'] = df['sku_code'].apply(lambda x: '{:03d}'.format(x))

for row in df.index:
    data = json.loads(df['spec_value'].at[row])
    color = data[0]['vname']
    size = data[1]['vname']
    df['spec_value'].at[row] = color + '-'+ size

# df1和df2不太一样
df1=df.pivot(index='sku_code',columns='spec_value',values='saleable_quantity').rename_axis(columns=None).reset_index()
df2 = df.T

print(df1)
print(df2)

df2.to_excel('xlsx/ods_ic_item_sku_17218746_pandas_output.xlsx')