import os
import sparkAPI

from dotenv import load_dotenv, find_dotenv

# 读取本地/项目的环境变量。

# find_dotenv() 寻找并定位 .env 文件的路径
# load_dotenv() 读取该 .env 文件，并将其中的环境变量加载到当前的运行环境中
# 如果你设置的是全局的环境变量，这行代码则没有任何作用。
_ = load_dotenv(find_dotenv())


def gen_spark_params(model):
    '''
    构造星火模型请求参数
    '''

    spark_url_tpl = "wss://spark-api.xf-yun.com/{}/chat"
    model_params_dict = {
        # v1.5 版本
        "v1.5": {
            "domain": "general",  # 用于配置大模型版本
            "spark_url": spark_url_tpl.format("v1.1")  # 云端环境的服务地址
        },
        # v2.0 版本
        "v2.0": {
            "domain": "generalv2",  # 用于配置大模型版本
            "spark_url": spark_url_tpl.format("v2.1")  # 云端环境的服务地址
        },
        # v3.0 版本
        "v3.0": {
            "domain": "generalv3",  # 用于配置大模型版本
            "spark_url": spark_url_tpl.format("v3.1")  # 云端环境的服务地址
        },
        # v3.5 版本
        "v3.5": {
            "domain": "generalv3.5",  # 用于配置大模型版本
            "spark_url": spark_url_tpl.format("v3.5")  # 云端环境的服务地址

        },
        # 4.0 Ultra 环境
        "v4.0": {
            "domain": "4.0Ultra",  # 用于配置大模型版本
            "spark_url": spark_url_tpl.format("v4.0")  # 云端环境的服务地址
        }
    }
    return model_params_dict[model]


def get_completion(prompt, model="v4.0", temperature=0.1):
    '''
    获取星火模型调用结果

    请求参数：
        prompt: 对应的提示词
        model: 调用的模型，默认为 v3.5，也可以按需选择 v3.0 等其他模型
        temperature: 模型输出的温度系数，控制输出的随机程度，取值范围是 0~1.0，且不能设置为 0。温度系数越低，输出内容越一致。
    '''

    response = sparkAPI.main(
        appid=os.environ["SPARK_APPID"],
        api_secret=os.environ["SPARK_API_SECRET"],
        api_key=os.environ["SPARK_API_KEY"],
        spark_url=gen_spark_params(model)["spark_url"],
        domain=gen_spark_params(model)["domain"],
        query=prompt
    )
    return response


get_completion("你好")
