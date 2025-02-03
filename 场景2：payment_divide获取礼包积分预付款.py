import pandas as pd
import re

# 假设这是你的JSON字符串
# json_str = 'payment_divide:[{div_total_fee:293;payment_flow_id:F20220706200111567610006959;div_item_amt:293;div_tax_amt:0;payment_id:P2022070601239201006959;pay_channel:10201;div_freight_amt:0};{div_total_fee:4207;payment_flow_id:F20220706200111567608006959;div_item_amt:4207;div_tax_amt:0;payment_id:P2022070601239201006959;pay_channel:10301;div_freight_amt:0};{div_total_fee:293;payment_flow_id:F20220706200057569581006959;div_item_amt:293;div_tax_amt:0;payment_id:P2022070601239201006959;pay_channel:10201;div_freight_amt:0};{div_total_fee:0;payment_flow_id:F20220706200057569582006959;div_item_amt:0;div_tax_amt:0;payment_id:P2022070601239201006959;pay_channel:20801;div_freight_amt:0}]'

# 定义解析函数
def parse_payment_divide(payment_divide):
    """
    解析 payment_divide 列，提取 pay_channel 和 div_total_fee
    """
    try:
        # 使用正则表达式提取每个段落
        segments = re.findall(r"\{.*?\}", payment_divide)
        results = []
        for segment in segments:
            # 提取键值对
            data = re.findall(r"(\w+):([^;]+)", segment)
            # 转换为字典
            segment_dict = {key: value for key, value in data}
            results.append(segment_dict)
        return results
    except Exception as e:
        print(f"解析错误: {e}")
        return []

# 定义提取函数
def extract_div_total_fee_10101(payment_divide, target_pay_channel="10101"):
    if pd.isna(payment_divide):
        return None
    # 提取 pay_channel 等于 target_pay_channel 的 div_total_fee
    try:
        parsed_data = parse_payment_divide(payment_divide)
        # 遍历解析后的数据，检查 pay_channel 是否等于目标值（如 10101）；如果匹配，提取 div_total_fee 并转换为整数
        div_total_fees = [int(segment["div_total_fee"]) for segment in parsed_data if segment.get("pay_channel") == target_pay_channel]
        return div_total_fees
    except Exception as e:
        print(f"提取错误: {e}")
        return [...]

# 定义提取函数
def extract_div_total_fee_10201(payment_divide, target_pay_channel="10201"):
    if pd.isna(payment_divide):
        return None
    # 提取 pay_channel 等于 target_pay_channel 的 div_total_fee
    try:
        parsed_data = parse_payment_divide(payment_divide)
        div_total_fees = [int(segment["div_total_fee"]) for segment in parsed_data if segment.get("pay_channel") == target_pay_channel]
        return div_total_fees
    except Exception as e:
        print(f"提取错误: {e}")
        return [...]

def extract_div_total_fee_10301(payment_divide, target_pay_channel="10301"):
    if pd.isna(payment_divide):
        return None
    # 提取 pay_channel 等于 target_pay_channel 的 div_total_fee
    try:
        parsed_data = parse_payment_divide(payment_divide)
        div_total_fees = [int(segment["div_total_fee"]) for segment in parsed_data if segment.get("pay_channel") == target_pay_channel]
        return div_total_fees
    except Exception as e:
        print(f"提取错误: {e}")
        return []

# 读取 Excel 文件
df = pd.read_excel("xlsx/tc_order_payment_divide_saveamt_deposit_count.xlsx", sheet_name="SheetJS", index_col="id")

# 应用函数到每一行
# 代码具有鲁棒性，能够处理复杂的非标准数据格式
df["10101"] = df["payment_divide"].apply(extract_div_total_fee_10101)
df["10201"] = df["payment_divide"].apply(extract_div_total_fee_10201)
df["10301"] = df["payment_divide"].apply(extract_div_total_fee_10301)

# 输出结果
print(df[["order_id", "10101", "10201", '10301']])