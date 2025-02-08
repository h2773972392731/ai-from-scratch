import pandas as pd

# 需求：按月求和赋予、使用、过期、其他扣减，期初用当月第一天的期初值，期末用当月最后一天的期末值
# 参考：3.审计\2024.12.03_天健审计\2025.01.07_老夏版本积分变动明细数据和积分成本查询页面数据匹配\积分成本查询页面数据生成SQL\【积分成本查询页面】2024年按月汇总数据\*.*

# 读取文件
excel_file = pd.ExcelFile('xlsx/2024年按天汇总数据.xlsx')

# 获取所有表名
sheet_names = excel_file.sheet_names
print(sheet_names)

# 获取指定工作表中的数据
df = excel_file.parse('SheetJS')

# 查看数据的基本信息
print('数据基本信息：')
df.info()

# 查看数据集行数和列数
rows, columns = df.shape

if rows < 100 and columns < 20:
    # 短表数据（行数少于100且列数少于20）查看全量数据信息
    print('数据全部内容信息：')
    print(df.to_csv(sep='\t', na_rep='nan'))
else:
    # 长表数据查看数据前几行信息
    print('数据前几行内容信息：')
    print(df.head().to_csv(sep='\t', na_rep='nan'))

# 将日期列转换为日期时间类型
df['日期'] = pd.to_datetime(df['日期'])

# 提取月份信息
df['月份'] = df['日期'].dt.to_period('M')

# 按月份分组，对赋予、使用、过期和其他扣减列求和，对期初列取每月第一天的值，对期末列取每月最后一天的值
summary = df.groupby('月份').agg({
    '期初': lambda x: x.iloc[0],
    '赋予': 'sum',
    '使用': 'sum',
    '过期': 'sum',
    '其他扣减': 'sum',
    '期末': lambda x: x.iloc[-1]
}).reset_index()

# 将结果保存为 Excel 文件
summary.to_excel('xlsx/2024年按月汇总数据_output.xlsx', index=False)