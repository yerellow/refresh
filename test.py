from selenium import webdriver
import time, random, datetime
import user_set as user
from selenium.webdriver.chrome.options import Options
import threading
import requests

url = 'https://www.zgcsb.com/news/shenDuBaoDao/2024-05/13/a_515362.html'
chromes = 2
times = 1
api = "https://dps.kdlapi.com/api/getdps/?secret_id=owb3f8sxl90bbpcr77za&signature=3pjrrzvs换成你自己的paapf2&num=20&pt=1&format=text&sep=1"
# 请求参数
params = {
    "secret_id": "owb3f8sxl90bbpcr77za",
    "signature": "3pjrrzvs2qe9d84veit051djw6paapf2",
    "num": 1,   # 提取数量
}
# url为待刷网页，chromes为打开浏览器的数量，times为浏览次数，chromes*times为总浏览量

# 获取响应内容
def get_proxy(api, params):
    # 调用API获取IP地址
    response = requests.get(api, params=params)
    if response.status_code == 200:
        print(response.text)
        proxies = response.text
        return proxies
def pv_pool(name, url, count, api, params):
    for i in range(count):
        headers = random.choice(user.UserAgent1)
        chrome_options = Options()
        chrome_options.add_argument('--disable-gpu')
        # chrome_options.add_argument('headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--user-agent=%s' % headers)
        chrome_options.add_argument('--ignore-certificate-errors')
        # 获取代理IP
        proxy = get_proxy(api, params)
        if proxy:
            chrome_options.add_argument(f'--proxy-server=http://{proxy}')

        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
        time.sleep(random.uniform(user.speed_low, user.speed_high))
        driver.quit()
        print("第 %d 次访问网页【%s】" % (i + 1, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    print('~~~~{}线程结束时间：{}~~~~~\n'.format(name, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))




if __name__ == '__main__':
    print('※※※※※线程启动时间：{}※※※※\n'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    start_time = time.time()
    # 创建并启动多个线程
    threads = []
    for i in range(chromes):
        thread = threading.Thread(target=pv_pool, args=(i+1, url, times, api, params))
        thread.start()
        threads.append(thread)

    # 等待所有线程执行完成
    for thread in threads:
        thread.join()
    c = chromes*times
    print(f"所有线程执行完成,共浏览{c}次")
    # 计算并打印用时
    elapsed_time = time.time() - start_time
    print(f"用时: {elapsed_time:.2f} 秒")
