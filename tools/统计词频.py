# 代码说明
# 预处理函数 (preprocess_text)：
# 根据语言选择不同的处理方式：
# 英文：去除标点符号、转换为小写、去除停用词。
# 中文：使用 jieba 分词，并去除单个字符和无意义字符。
# 词频统计函数 (count_word_frequencies)：
# 使用 collections.Counter 统计单词频率。
# 展示高频词函数 (display_top_n_words)：
# 按词频排序，并输出前 N 个高频词。
# 主程序：
# 分别对英文和中文文本进行词频统计，并展示结果。

import re
from collections import Counter
import jieba  # 用于中文分词
from nltk.corpus import stopwords  # 用于英文停用词过滤
import matplotlib.pyplot as plt

# 如果是第一次使用 NLTK 的 stopwords，请先下载
import nltk
from pprint import pprint

# nltk.download('stopwords')
# nltk.download('all')

# 查看所有已下载的数据包
# pprint(nltk.data.find("corpora").listdir())


def preprocess_text(text, language='en'):
    """
    预处理文本：去除标点符号、转换为小写、分词等。
    :param text: 输入文本
    :param language: 文本语言 ('en' 或 'zh')
    :return: 处理后的单词列表
    """
    if language == 'en':
        # 英文处理：去除标点符号、转换为小写
        words = re.findall(r'\b\w+\b', text.lower())
        # 去除停用词
        stop_words = set(stopwords.words('english'))
        words = [word for word in words if word not in stop_words]
    elif language == 'zh':
        # 中文处理：使用 jieba 分词
        words = list(jieba.lcut(text))
        # 去除单个字符和无意义字符
        words = [word for word in words if len(word) > 1 and re.match(r'^[\u4e00-\u9fff]+$', word)]
    else:
        raise ValueError("Unsupported language. Use 'en' for English or 'zh' for Chinese.")
    return words


def count_word_frequencies(words):
    """
    统计词频。
    :param words: 单词列表
    :return: 单词频率的 Counter 对象
    """
    return Counter(words)


def display_top_n_words(word_count, n=10):
    """
    显示前 N 个高频词。
    :param word_count: 单词频率的 Counter 对象
    :param n: 显示的高频词数量
    """
    print(f"Top {n} most frequent words:")
    for word, freq in word_count.most_common(n):
        print(f"{word}: {freq}")


# 可以从多个文件中读取文本内容，合并后进行统计
def read_and_process_files(file_paths, language='en'):
    all_words = []
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            words = preprocess_text(text, language=language)
            all_words.extend(words)
    return all_words


# 使用 matplotlib 或 seaborn 绘制词频柱状图
def plot_word_frequencies(word_count, n=10):
    words, frequencies = zip(*word_count.most_common(n))
    plt.bar(words, frequencies)
    plt.xlabel('Words')
    plt.ylabel('Frequencies')
    plt.title(f'Top {n} Most Frequent Words')
    plt.xticks(rotation=45)
    plt.show()


# 将统计结果保存到文件中
def save_word_frequencies(word_count, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        for word, freq in word_count.items():
            file.write(f"{word}: {freq}\n")


# 示例：统计英文文本的词频
if __name__ == "__main__":
    # 示例英文文本
    english_text = """
    Hello world! This is a test. Hello Python programming. World, hello code.
    Programming is fun, and coding is cool. Let's write some code today!
    """

    # 示例中文文本
    chinese_text = """
    今天天气很好，我们一起去公园散步。公园里有很多人，有的在跑步，有的在聊天。
    大家都很开心，享受着美好的时光。希望每天都能有这样的好天气！
    """

    # 英文词频统计
    print("English Word Frequency Analysis:")
    english_words = preprocess_text(english_text, language='en')
    english_word_count = count_word_frequencies(english_words)
    display_top_n_words(english_word_count, n=5)

    print("\n" + "-" * 50 + "\n")

    # 中文词频统计
    print("Chinese Word Frequency Analysis:")
    chinese_words = preprocess_text(chinese_text, language='zh')
    chinese_word_count = count_word_frequencies(chinese_words)
    display_top_n_words(chinese_word_count, n=5)
