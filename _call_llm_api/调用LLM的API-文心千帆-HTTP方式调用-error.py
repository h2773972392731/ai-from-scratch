import qianfan


def gen_wenxin_messages(prompt):
    '''
    构造文心模型请求参数 messages

    请求参数：
        prompt: 对应的用户提示词
    '''
    messages = [{"role": "user", "content": prompt}]
    return messages


def get_completion(prompt, model="ERNIE-Bot", temperature=0.01):
    '''
    获取文心模型调用结果

    请求参数：
        prompt: 对应的提示词
        model: 调用的模型，默认为 ERNIE-Bot，也可以按需选择 ERNIE-Bot-4 等其他模型
        temperature: 模型输出的温度系数，控制输出的随机程度，取值范围是 0~1.0，且不能设置为 0。温度系数越低，输出内容越一致。
    '''

    chat_comp = qianfan.ChatCompletion()
    message = gen_wenxin_messages(prompt)

    resp = chat_comp.do(messages=message,
                        model=model,
                        temperature=temperature,
                        system="你是一名个人助理-小鲸鱼")

    return resp["result"]


get_completion("你好，介绍一下你自己", model="Yi-34B-Chat")
