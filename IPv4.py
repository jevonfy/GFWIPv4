import requests
from bs4 import BeautifulSoup
import re

# 发送HTTP请求并获取网页内容
url = "https://zh.wikiversity.org/wiki/%E9%98%B2%E7%81%AB%E9%95%BF%E5%9F%8E%E5%9F%9F%E5%90%8D%E6%9C%8D%E5%8A%A1%E5%99%A8%E7%BC%93%E5%AD%98%E6%B1%A1%E6%9F%93IP%E5%88%97%E8%A1%A8"
response = requests.get(url)
html_content = response.text

# 使用BeautifulSoup解析HTML
soup = BeautifulSoup(html_content, "html.parser")

# 找到目标内容所在的div标签
div_content = soup.find("div", class_="mw-highlight mw-highlight-lang-text mw-content-ltr mw-highlight-lines")

# 找到div标签下的pre标签
pre_tags = div_content.find_all("pre")

# 提取并处理数据
ip_list = []
for pre in pre_tags:
    # 使用正则表达式匹配符合形式的数据
    ips = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", pre.text)
    ip_list.extend(ips)

# 去除空白行
ip_list = [ip for ip in ip_list if ip.strip()]

# 将数据写入txt文件
with open("ip_list.txt", "w") as file:
    for ip in ip_list:
        file.write(ip + "\n")

print("数据已成功写入ip_list.txt文件！")
