import zipfile
import itertools
import string


def crack_zip_password(zip_path):
    # 设置zip文件路径
    zip_file = zipfile.ZipFile(zip_path)

    # 定义可能的字符集（仅数字）
    characters = string.digits  # '0123456789'

    print("开始破解密码...")

    # 只尝试4位和6位密码
    for length in [4, 6]:
        print(f"正在尝试 {length} 位密码...")
        # 生成当前长度的所有可能密码组合
        for password in itertools.product(characters, repeat=length):
            # 将元组转换为字符串
            password_str = ''.join(password)

            try:
                # 尝试使用当前密码解压
                zip_file.extractall(pwd=password_str.encode())
                print(f"成功找到密码：{password_str}")
                return password_str
            except Exception:
                # 密码错误，继续尝试下一个
                continue

    print("未能在4位或6位密码中找到正确密码")
    return None


# 使用示例
if __name__ == "__main__":
    # 替换为你的zip文件路径
    zip_file_path = "F:/xyzml.zip"
    found_password = crack_zip_password(zip_file_path)
