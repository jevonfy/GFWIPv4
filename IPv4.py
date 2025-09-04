import re
import requests
from bs4 import BeautifulSoup

# 目标 URL
url = "https://zh.wikiversity.org/wiki/%E9%98%B2%E7%81%AB%E9%95%BF%E5%9F%8E%E5%9F%9F%E5%90%8D%E6%9C%8D%E5%8A%A1%E5%99%A8%E7%BC%93%E5%AD%98%E6%B1%A1%E6%9F%93IP%E5%88%97%E8%A1%A8"

headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

# 找到所有 <pre> 标签
pre_tags = soup.find_all("pre")

if not pre_tags:
    print("未找到任何 <pre> 标签")
else:
    ipv4_pattern = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')
    ipv6_pattern = re.compile(r'\b(?:[0-9a-fA-F]{1,4}:){1,7}[0-9a-fA-F]{1,4}\b')

    ipv4_list = []
    ipv6_list = []

    # 遍历每个 <pre>，按原顺序提取 IP
    for pre in pre_tags:
        text = pre.get_text()
        ipv4_list.extend(ipv4_pattern.findall(text))
        ipv6_list.extend(ipv6_pattern.findall(text))

    # 去重且保持顺序
    ipv4_list = list(dict.fromkeys(ipv4_list))
    ipv6_list = list(dict.fromkeys(ipv6_list))

    # 写入文件：先 IPv4，再 IPv6
    with open("ip_list.txt", "w", encoding="utf-8") as f:
        for ip in ipv4_list:
            f.write(ip + "\n")
        for ip in ipv6_list:
            f.write(ip + "\n")

    print(f"已将 {len(ipv4_list)} 个 IPv4 和 {len(ipv6_list)} 个 IPv6 写入 ip_list.txt（已去重）")
