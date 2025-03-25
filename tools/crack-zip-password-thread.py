import zipfile
import itertools
import string
import threading
from concurrent.futures import ThreadPoolExecutor
import time


def try_password(zip_file, password_str, result):
    """尝试单个密码"""
    try:
        zip_file.extractall(pwd=password_str.encode())
        result['password'] = password_str
        return True
    except Exception:
        return False


def crack_zip_password(zip_path, max_workers=4):
    # 设置zip文件路径
    zip_file = zipfile.ZipFile(zip_path)

    # 定义可能的字符集（仅数字）
    characters = string.digits  # '0123456789'

    # 用于存储结果的字典
    result = {'password': None}

    print("开始破解密码...")

    # 只尝试4位和6位密码
    for length in [4, 6]:
        print(f"\n正在尝试 {length} 位密码...")

        # 计算总密码数量
        total_combinations = len(characters) ** length
        attempted = 0
        chunk_size = 10000  # 每块处理的密码数量

        # 生成密码组合
        password_generator = itertools.product(characters, repeat=length)

        start_time = time.time()

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            while attempted < total_combinations:
                # 获取一批密码
                passwords_chunk = [''.join(p) for p in itertools.islice(password_generator, chunk_size)]
                if not passwords_chunk:
                    break

                # 使用多线程尝试这批密码
                futures = {executor.submit(try_password, zip_file, pwd, result): pwd
                           for pwd in passwords_chunk}

                # 检查是否有成功结果
                for future in futures:
                    if future.result():
                        print(f"\n成功找到密码：{result['password']}")
                        return result['password']

                # 更新进度
                attempted += len(passwords_chunk)
                progress = (attempted / total_combinations) * 100
                elapsed_time = time.time() - start_time
                if attempted > 0:
                    speed = attempted / elapsed_time
                    eta = (total_combinations - attempted) / speed if speed > 0 else 0
                    print(f"\r进度: {progress:.2f}% ({attempted}/{total_combinations}) | "
                          f"速度: {speed:.0f} 密码/秒 | ETA: {eta:.0f}秒", end="")

                if result['password']:
                    print(f"\n成功找到密码：{result['password']}")
                    return result['password']

        print(f"\n{length}位密码尝试完成")

    print("\n未能在4位或6位密码中找到正确密码")
    return None


# 使用示例
if __name__ == "__main__":
    # 替换为你的zip文件路径
    zip_file_path = "F:/xyzml.zip"
    found_password = crack_zip_password(zip_file_path, max_workers=4)  # 可调整线程数
