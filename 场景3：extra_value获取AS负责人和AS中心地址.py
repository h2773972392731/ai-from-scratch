import json
import pandas as pd

# 假设你有一个 JSON 字符串
# data = '[{"id":1000752,"name":"(部分)更换时注意事项","value":"无质量问题不得更换，若只是配件有问题，则更换部分配件，不更换整套产品。陶瓷盆有伸缩率，误差尺寸在0.5-2cm之间"},{"id":1000753,"name":"A/S中心地址","value":"上海市普陀区丹巴路1238号E座1201室 "},{"id":1000754,"name":"A/S中心地址","value":"产品咨询、预约送货和安装电话：021-60799312，021-61906596（周一到周日9:30-17:30）；报修电话：4007888758（周一到周五9点30-17点30）"},{"id":1000755,"name":"A/S服务时间","value":"周一至周五9：30-17：30"},{"id":1000756,"name":"产品可否修理","value":"是"},{"id":1000758,"name":"供应公司A/S负责人","value":"叶雨、13482288150"},{"id":1000759,"name":"免费保修期限","value":"1年"},{"id":1000760,"name":"特点","value":""},{"id":1000761,"name":"订购接收时注意事项","value":"1.本产品采用券配送方式；提醒顾客务必将券妥善保管，不得遗失，无券不配送产品\n2.提供免费测量，送货、拆旧、安装服务（安装服务2年内有效，包含赠品龙头，若龙头和浴室柜安装在两个不同地址，则龙头安装需另外收费）\n3．该款式分100/90/80/70cm四个标准尺寸可选，贝朗工作人员测量后给顾客决定尺寸"},{"id":1000762,"name":"订购接收时注意事项(物流)","value":""},{"id":1000763,"name":"退货时注意事项","value":"1.浴室柜实物送货完成，无质量问题，不予退货.\n2.产品完成安装后，经顾客签字验收不予退货.\n3.发现产品包装已拆封并有使用迹象，且产品破损或零件缺失的不予退货（根据实际情况可进行换货或更换零件）.\n4.出现下述情况，安装人员必须将风险告知顾客。如顾客仍坚持选择安装，需签字确认并承担相应风险，且不予退货.a)现场墙体情况不明，可能引起水管爆裂或者线路损坏等问题.b）现场墙面材质问题或墙面老化，可能引起墙面瓷砖破裂问题.c）产品尺寸，安装效果不理想.\n5.由于顾客自身体验感觉或是操作使用不当问题，造成要求换货和退货的，在给于顾客指导和解释的同时。明确非产品质量问题一律不予换货或退货"},{"id":1000764,"name":"配送/包装形态详情","value":"OCJ券配送"}]'

def get_extra_value_as_address(extra_value):
    if pd.isna(extra_value):
        return None

    extra_value = extra_value.replace('\n', '\\n')

    items = json.loads(extra_value)

    # 查找 name 为 "A/S中心地址" 的 value 值
    # 货号：17128943，as_addresses会生成出如下格式
    # ['上海市普陀区丹巴路1238号E座1201室 ','产品咨询、预约送货和安装电话：021-60799312，021-61906596（周一到周日9:30-17:30）；报修电话：4007888758（周一到周五9点30-17点30）']
    # 列表推导式。这个列表推导式遍历了items中的每个item。对于每个item，它检查item["name"]是否等于"A/S中心地址"。如果满足这个条件，那么就会取出item["value"]，并将这些值组成一个新的列表，赋值给as_addresses变量
    as_addresses = [item["value"] for item in items if item["name"] == "A/S中心地址"]

    # 货号：17128943，as_addresses2会生成出如下格式
    # 上海市普陀区丹巴路1238号E座1201室;产品咨询、预约送货和安装电话：021 - 60799312，021 - 61906596（周一到周日9: 30 - 17:30）；报修电话：4007888758（周一到周五9点30 - 17点30）
    # 用于lateral view explode(split(as_addresses2,';')) temp as divide
    as_addresses2 = build_string(as_addresses)

    # 可以返回两种格式的A/S中心地址
    # return as_addresses
    return as_addresses2

# 构建字符串，格式：address1:上海市普陀区丹巴路1238号E座1201室;address2:产品咨询、预约送货和安装电话：021-6。用于再次导入数据库，用lateral view explode进行列转行
def build_string(parts):
    result = ";".join(parts)
    return result

def get_extra_value_as_person_in_charge(extra_value):
    if pd.isna(extra_value):
        return None

    # extra_value中存在\n
    extra_value = extra_value.replace('\n', '\\n')

    items = json.loads(extra_value)

    # 查找 name 为 "供应公司A/S负责人" 的 value 值
    as_persons = [item["value"] for item in items if item["name"] == "供应公司A/S负责人"]

    return as_persons

pd.options.display.max_columns = 999

df = pd.read_excel("xlsx/ic_item_extra.extra_value.xlsx", sheet_name="SheetJS")

df['A/S中心地址'] = df['extra_value'].apply(get_extra_value_as_address)
df['供应公司A/S负责人'] = df['extra_value'].apply(get_extra_value_as_person_in_charge)

print(df[["货号", "A/S中心地址", "供应公司A/S负责人"]])

# df.to_excel('xlsx/ic_item_extra.extra_value_output.xlsx')