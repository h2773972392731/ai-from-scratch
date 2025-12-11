# -*- coding: utf-8 -*-
"""
一键解析出团信息（带中文状态翻译版）
双击运行 → 选择你的 Excel → 自动在同目录生成“xxx_已解析出团信息.xlsx”
"""

import pandas as pd
import json
import os
from tkinter import filedialog, Tk

# ==================== 1. 弹窗选择文件 ====================
Tk().withdraw()  # 隐藏 Tk 主窗口
print("请在弹出的窗口中选择要解析的 Excel 文件...")
file_path = filedialog.askopenfilename(
    title="请选择包含【出团信息】列的 Excel 文件",
    filetypes=[("Excel 文件", "*.xlsx *.xls"), ("所有文件", "*.*")]
)

if not file_path:
    print("未选择文件，程序已退出。")
    input("按回车关闭窗口...")
    exit()

print(f"正在处理文件：{file_path}")

# ==================== 2. 读取原始数据 ====================
try:
    df = pd.read_excel(file_path, sheet_name="SheetJS")
except Exception as e:
    print(f"读取 Excel 失败：{e}")
    input("按回车关闭...")
    exit()

# ==================== 3. 状态映射字典 ====================
state_map = {
    0: "报名中",
    1: "已成团",
    2: "已结束"
}

# ==================== 4. 解析并展开出团信息 ====================
expanded_rows = []

for idx, row in df.iterrows():
    json_str = row['出团信息']
    try:
        data = json.loads(json_str)
        for item in data['comeOutMessage']:
            new_row = row.copy()
            new_row['计划人数'] = item['comeOutCount']
            new_row['团期状态'] = state_map.get(item['comeOutSate'], f"未知状态({item['comeOutSate']})")
            new_row['出团日期'] = item['comeOutTime']
            expanded_rows.append(new_row)
    except Exception as e:
        print(f"第 {idx+2} 行解析失败，已保留原行不展开：{e}")
        expanded_rows.append(row)

# ==================== 5. 生成新 DataFrame ====================
result_df = pd.DataFrame(expanded_rows)

# 把三列插入到“出团信息”列的后面
orig_cols = list(df.columns)
try:
    insert_pos = orig_cols.index('出团信息') + 1
except ValueError:
    insert_pos = len(orig_cols)

new_order = (
    orig_cols[:insert_pos] +
    ['计划人数', '团期状态', '出团日期'] +
    orig_cols[insert_pos:]
)
result_df = result_df[new_order]

# ==================== 6. 保存新文件（同目录） ====================
dir_name = os.path.dirname(file_path)
base_name = os.path.basename(file_path)
name, ext = os.path.splitext(base_name)
output_path = os.path.join(dir_name, f"{name}_已解析出团信息{ext}")

result_df.to_excel(output_path, index=False)

print("\n" + "="*50)
print("处理完成！")
print(f"原订单数：{len(df)} 条")
print(f"展开后团期数：{len(result_df)} 条")
print(f"已自动保存到：")
print(output_path)
print("="*50)
input("按回车键关闭窗口...")