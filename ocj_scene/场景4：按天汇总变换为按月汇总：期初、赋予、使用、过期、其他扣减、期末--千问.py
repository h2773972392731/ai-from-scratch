import pandas as pd

# 需求：按月求和赋予、使用、过期、其他扣减，期初用当月第一天的期初值，期末用当月最后一天的期末值
# 参考：3.审计\2024.12.03_天健审计\2025.01.07_老夏版本积分变动明细数据和积分成本查询页面数据匹配\积分成本查询页面数据生成SQL\【积分成本查询页面】2024年按月汇总数据\*.*
# 问千问，prompt:附件中，请按月汇总赋予，使用，过期，其他扣减列的总金额，但按月汇总后的期初和期末列，期初用当月第一天的期初值，期末用当月最后一天的期末值，请提供python脚本

# 读取Excel文件
file_path = '../xlsx/2024年按天汇总数据_origin.xlsx'
df = pd.read_excel(file_path, engine='openpyxl')

# 将日期列转换为datetime类型
df['日期'] = pd.to_datetime(df['日期'])

# 设置日期为索引
df.set_index('日期', inplace=True)

# 按月重新采样数据并计算每月的总和
monthly = df.resample('ME').agg({
    '期初': 'first',
    '赋予': 'sum',
    '使用': 'sum',
    '过期': 'sum',
    '其他扣减': 'sum',
    '期末': 'last'
})

# 打印结果或保存到新的Excel文件中
print(monthly)
# 若要保存到新的Excel文件，可以取消下面注释
monthly.to_excel('xlsx/2024年按月汇总数据_千问_output.xlsx')