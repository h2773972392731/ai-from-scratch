from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

# 配置无头浏览器（可选）
chrome_options = Options()
chrome_options.add_argument('--headless')  # 无界面运行

# 启动浏览器
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://grok.com/share/bGVnYWN5_70abd8e4-755a-4bda-a53a-fc58419464e8')  # 替换为实际URL

# 等待页面加载（可能需要调整时间）
time.sleep(5)

# 滚动页面加载所有内容（示例）
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # 等待加载
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# 获取页面HTML
html_content = driver.page_source

# 使用BeautifulSoup解析并保存为Markdown（复用上述代码）
soup = BeautifulSoup(html_content, 'html.parser')
with open('e:/grok_chat2.md', 'w', encoding='utf-8') as f:
    for user_msg in soup.find_all('div', class_='user'):
        text = user_msg.get_text().strip()
        f.write(f"- {text}\n\n")
    for grok_msg in soup.find_all('div', class_='grok'):
        text = grok_msg.get_text().strip()
        f.write(f"> {text}\n\n")

# 关闭浏览器
driver.quit()
print("对话内容已成功保存为 grok_chat.md 文件！")