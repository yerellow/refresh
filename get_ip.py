import requests
import user_set as user
from lxml import etree
import time, random
import re
import json


iplist = []
# 获取私密代理IP API
api = "https://dps.kdlapi.com/api/getdps/?secret_id=owb3f8sxl90bbpcr77za&signature=3pjrrzvs2qe9d84veit051djw6paapf2&num=20&pt=1&format=text&sep=1"

# 请求参数
params = {
    "secret_id": "owb3f8sxl90bbpcr77za",
    "signature": "3pjrrzvs2qe9d84veit051djw6paapf2",
    "num": 1,   # 提取数量
}
def get_proxy(api, params):
    # 调用API获取IP地址
    response = requests.get(api, params=params)
    if response.status_code == 200:
        print(response.text)
        proxies = response.text.strip().split('\n')
        return proxies
# 获取响应内容

ipall = []
for i in iplist:
    proxies = {
        'http': ''
    }
    headers = random.choice(user.UserAgent1)
    proxies['http'] = i
    try:
        response = requests.get('https://www.zgcsb.com/news/shenDuBaoDao/2024-05/13/a_515362.html', headers=headers, proxies=proxies, timeout=2)
        time.sleep(1)
        if response.status_code == 200:
            ipall.append(i)
        else:
            print(response.status_code)
    except:
        pass
print(ipall)

    # ip = html.xpath('//*[@id="list"]/table/tbody/tr/td[1]')
    # port = html.xpath('//*[@id="list"]/table/tbody/tr/td[2]')
    # print(ip)
    # print(port)

    # if match:
    #     fps_list_str = match.group(1)
    #     # 将提取的字符串转换为 JSON 对象
    #     fps_list = json.loads(fps_list_str)
    #     print(fps_list)
    # else:
    #     print("fpsList not found in the script.")
# def get_ip(page):
#     """获取ip"""
#     proxies = {
#         'http':'快代理被墙了，需要VPN才可以访问'
#     }
#
#     for i in range(1,page+1):
#         headers = {
#             'User-Agent':random.choice(user.UserAgent1)
#         }
#         response = requests.get(f'https://www.kuaidaili.com/free/inha/{i}',headers=headers,proxies=proxies)
#         #print(response.status_code)
#         html=etree.HTML(response.text)
#         #print(html)
#         ip=html.xpath('//*[@id="list"]/table/tbody/tr/td[1]')
#         port = html.xpath('//*[@id="list"]/table/tbody/tr/td[2]')
#         print(ip)
#         print(port)
#         break
#         for a,b in zip(ip,port):
#             a1=a.text
#             b1=b.text
#             c = a1 + ':' + b1
#             ips.append(c)
#         time.sleep(2)