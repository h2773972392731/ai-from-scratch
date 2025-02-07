import pandas as pd

# 参考：3.审计\2024.12.03_天健审计\2025.01.07_老夏版本积分变动明细数据和积分成本查询页面数据匹配\积分成本查询页面数据生成SQL\积分成本查询(按月汇总).sql

# 读取Excel文件
file_path = "xlsx/2024年按天汇总数据.xlsx"  # 替换为实际文件路径
sheet_name = "SheetJS"  # 根据metadata.sheet_name指定

# 读取指定工作表数据
df = pd.read_excel(file_path,
                   sheet_name=sheet_name,
                   skiprows=2,  # 跳过前两行非数据行(根据实际文件结构调整)
                   usecols="A:G"  # 读取A到G列
                   )

# 重命名列（根据实际列名调整）
df.columns = ["日期", "期初", "赋予", "使用", "过期", "其他扣减", "期末"]

# 转换日期格式
df["日期"] = pd.to_datetime(df["日期"])

# 按月份分组
grouped = df.groupby(pd.Grouper(key="日期", freq="ME"))


# 定义聚合逻辑
def get_month_start(col):
    """获取每月第一天的值"""
    return lambda x: x.loc[x.index.min().replace(day=1)] if not x.empty else None


def get_month_end(col):
    """获取每月最后一天的值"""
    return lambda x: x.iloc[-1] if not x.empty else None


# 执行聚合计算
result = grouped.agg({
    # "期初": get_month_start("期初"),
    "赋予": "sum",
    "使用": "sum",
    "过期": "sum",
    "其他扣减": "sum",
    "期末": get_month_end("期末")
})

# 重置索引并格式化
result = result.reset_index()
result["月份"] = result["日期"].dt.strftime("%Y-%m")
# result = result[["月份", "期初", "赋予", "使用", "过期", "其他扣减", "期末"]]
result = result[["月份", "赋予", "使用", "过期", "其他扣减", "期末"]]

# 输出结果
print(result)

# 可选：保存到新Excel文件
result.to_excel("xlsx/2024年按月汇总数据_output.xlsx", index=False)
