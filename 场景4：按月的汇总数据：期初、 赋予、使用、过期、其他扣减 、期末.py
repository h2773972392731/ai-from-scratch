import pandas as pd

# 读取数据（假设数据已加载到DataFrame df中）
# 示例数据加载（根据实际数据来源调整）：
data = [
    # 这里替换为实际数据，格式如：
    ["2024-01-01", 10420539.21, 1300495.13, 325448.45, 54268.91, 27089.01, 11314227.97],
    ["2024-01-02", 11314227.97, 346164.54, 225737.21, 27140.63, 29173.58, 11378341.09]
    # ...
]
columns = ["日期", "期初", "赋予", "使用", "过期", "其他扣减", "期末"]
df = pd.DataFrame(data, columns=columns)

# 转换日期列为datetime类型
df["日期"] = pd.to_datetime(df["日期"])

# 按月份分组
grouped = df.groupby(pd.Grouper(key="日期", freq="M"))

# 定义聚合函数
def get_first_day_value(series):
    """获取当月第一天的值"""
    first_day = series.index.min().replace(day=1)
    return series.loc[first_day] if first_day in series.index else None

def get_last_day_value(series):
    """获取当月最后一天的值"""
    return series.iloc[-1] if not series.empty else None

# 执行聚合操作
result = grouped.agg({
    "期初": lambda x: get_first_day_value(df.set_index("日期")["期初"]),
    "赋予": "sum",
    "使用": "sum",
    "过期": "sum",
    "其他扣减": "sum",
    "期末": lambda x: get_last_day_value(df.set_index("日期")["期末"])
}).reset_index()

# 重命名列并格式化日期
result = result.rename(columns={"日期": "月份"})
result["月份"] = result["月份"].dt.strftime("%Y-%m")

# 确保列顺序
result = result[["月份", "期初", "赋予", "使用", "过期", "其他扣减", "期末"]]

print(result)