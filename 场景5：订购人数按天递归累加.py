# 报表-业务线报表-顾客分析-顾客订购汇总的订购人数
# 订购人数递归累加
# 数据1：先取每天的订购人数，1.1-1.31每天的数据先得到，然后递归累加：1.1，1.1+1.2，1.1+1.2+1.3，1.1+1.2+1.3+1.4......
# 详见：D:\1.工作文档\2.NERP\3.RUN\2023年历史顾客数据需求(2种递归累加2023年全年订购人数)--韩立存.sql

import pandas as pd

# 读取Excel文件
file_path = 'xlsx/订购顾客数明细.xlsx'
df = pd.read_excel(file_path)

# 将订购日期转换为日期格式
df['订购日期'] = pd.to_datetime(df['订购日期'])

# 定义时间范围（例如：2023-01-01 到 2023-01-03）
start_date = '2023-01-01'
end_date = '2023-02-28'

# 筛选指定时间范围内的数据
filtered_df = df[(df['订购日期'] >= start_date) & (df['订购日期'] <= end_date)]

# 初始化一个空的列表用于存储去重后的数据
deduplicated_data_list = []

# 按订购日期逐日处理，确保每天的数据独立去重
for date, group in filtered_df.groupby('订购日期'):
    # 在当天数据中去除重复的顾客编号，保留每名顾客最早的一次订购记录
    deduplicated_group = group.drop_duplicates(subset=['顾客编号'], keep='first')
    if not deduplicated_group.empty:  # 确保分组数据不为空
        deduplicated_data_list.append(deduplicated_group)

# 合并不为空的数据
if deduplicated_data_list:
    deduplicated_data = pd.concat(deduplicated_data_list, ignore_index=True)
else:
    deduplicated_data = pd.DataFrame(columns=filtered_df.columns)

# 按订购日期分组并统计每天的订购顾客数
daily_counts = deduplicated_data.groupby('订购日期').size().reset_index(name='daily_customers')

# 计算累计订购顾客数
daily_counts['cumulative_customers'] = daily_counts['daily_customers'].cumsum()

# 调整注册日期的显示格式为 YYYY-MM-DD
daily_counts['订购日期'] = daily_counts['订购日期'].dt.strftime('%Y-%m-%d')

# 输出结果
print(daily_counts)

# 如果需要保存结果到新的Excel文件
output_file_path = 'xlsx/订购顾客数明细_output.xlsx'
daily_counts.to_excel(output_file_path, index=False)
print(f"结果已保存到 {output_file_path}")