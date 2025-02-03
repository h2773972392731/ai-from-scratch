import pandas as pd
import numpy as np

# 数据库导出大批量数据到excel -> 利用excel功能进行数据处理 -> 手工再进行一次简单的数据处理 ->

# 读取 Excel 文件
# 显示前五行数据
# print("显示前五行数据")
# df = pd.read_excel('E:\2025-01-03-17-50-44_EXPORT_XLSX_17199018_302_0.xlsx')
# print(df.head())
#
# # 读取特定工作表
# print("读取特定工作表")
# df = pd.read_excel('2025-01-03-17-50-44_EXPORT_XLSX_17199018_302_0.xlsx', sheet_name='导出结果')
# print(df.head())
#
# # 选择特定列：
# print("选择特定列")
# df = pd.read_excel('2025-01-03-17-50-44_EXPORT_XLSX_17199018_302_0.xlsx', usecols=['订购编号','订购时间','category_price'])
# print(df.head())

pd.options.display.max_columns = 999


def change_assets_great_than(a):
    return a >= 9000


def change_type_equal(s):
    return s == 50001081


# 过滤数据：
print("过滤数据")
df = pd.read_excel('执行结果1 (65).xlsx', index_col='id')
# filtered_df = df[df['change_assets'] > 20]
# df = df.loc[df.change_assets.apply(change_assets_great_than)].loc[df.change_type.apply(change_type_equal)]
df = df.loc[df['change_assets'].apply(change_assets_great_than)].loc[df['change_type'].apply(change_type_equal)]
# df = df.loc[df['change_assets'].apply(lambda a: a >= 9000)].loc[df['change_type'].apply(lambda s: s == 50001081)]
print(df)

# 取个别列的数据
print("取个别列的数据")
df = pd.read_excel('执行结果1 (65).xlsx', index_col='id')
temp = df[['book_id', 'change_assets']]
print(temp)

# 生成EXCEL那样的透视表（用SQL很难实现）
print("生成EXCEL那样的透视表")
df = pd.read_excel('执行结果1 (65).xlsx', index_col='id')
df['Year'] = pd.DatetimeIndex(df['create_time']).year

pt1 = df.pivot_table(index='cust_id', columns='Year', values='change_assets', aggfunc=np.sum)
print(pt1)

pt1.to_excel('output.xlsx', index=True)

# GROUP BY（更像是用SQL写的那种）
print("GROUP BY")
df = pd.read_excel('执行结果1 (65).xlsx', index_col='id')
df['Year'] = pd.DatetimeIndex(df['create_time']).year

groups = df.groupby(['cust_id', 'Year'])
s = groups['change_assets'].sum()
c = groups['book_id'].count()

pt2 = pd.DataFrame({'Sum': s, 'Count': c})
print(pt2)

# 数据排序：
# print("数据排序")
# df = pd.read_excel('2025-01-03-17-50-44_EXPORT_XLSX_17199018_302_0.xlsx')
# sorted_df = df.sort_values(by='订购编号', ascending=False)
# print(sorted_df)

# # 数据分组：
# print("数据分组")
# df = pd.read_excel('2025-01-03-17-50-44_EXPORT_XLSX_17199018_302_0.xlsx')
# grouped_df = df.groupby('订购渠道').mean()
# print(grouped_df)
#
# # 添加新列：
# print("添加新列")
# df = pd.read_excel('2025-01-03-17-50-44_EXPORT_XLSX_17199018_302_0.xlsx')
# df['NewColumn'] = df['订购渠道'] * 2
# print(df)
#
# # 更新单元格：
# print("更新单元格")
# df = pd.read_excel('2025-01-03-17-50-44_EXPORT_XLSX_17199018_302_0.xlsx')
# df.at[0, '金额'] = 25
# print(df)
#
# # 删除列：
# print("删除列")
# df = pd.read_excel('2025-01-03-17-50-44_EXPORT_XLSX_17199018_302_0.xlsx')
# del df['积分消耗']
# print(df)
#
# # 合并多个Excel文件：
# # df1 = pd.read_excel('file1.xlsx')
# # df2 = pd.read_excel('file2.xlsx')
# # merged_df = pd.concat([df1, df2], ignore_index=True)
# # print(merged_df)
#
# # 数据透视表：
# print("数据透视表")
# df = pd.read_excel('2025-01-03-17-50-44_EXPORT_XLSX_17199018_302_0.xlsx')
# pivot_table = pd.pivot_table(df, values='积分消耗', index=['配送模式'], aggfunc='sum')
# print(pivot_table)
