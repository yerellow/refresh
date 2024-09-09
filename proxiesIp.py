import telnetlib
import requests

test_url = 'https://www.baidu.com'


# ip 检测，存储有效 ip地址
def ip_is_alive(ip_port):
    ip, port = ip_port[0], ip_port[1]
    try:
        tn = telnetlib.Telnet(ip, port=port, timeout=3)
    except:
        print('[-]无效ip:{}:{}'.format(ip, port))
    else:
        proxies = ip + ':' + port
        try:
            res = requests.get(test_url, proxies={"http": proxies, "https": proxies}, timeout=1)
        except:
            print('[-]无效ip:{}:{}'.format(ip, port))
        else:
            if res.status_code == 200:
                print('[+]有效ip:{}:{}'.format(ip, port))
                # 将有效 ip 写入文件中
                with open('ipporxy.txt', 'a+') as f:
                    f.write(ip + ':' + port + '\n')
#

# import socket
# import requests
#
# test_url = 'https://www.zgcsb.com/news/shenDuBaoDao/2024-05/13/a_515362.html'
#
# def ip_is_alive(ip_port):
#     ip, port = ip_port[0], ip_port[1]
#     try:
#         # Create a socket object
#         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         # Set a timeout for the connection attempt
#         s.settimeout(3)
#         # Attempt to connect to the IP address and port
#         s.connect((ip, port))
#         # If the connection is successful, attempt to make a request using the IP as a proxy
#         proxies = ip + ':' + port
#         try:
#             res = requests.get(test_url, proxies={"http": proxies, "https": proxies}, timeout=1)
#         except:
#             print('[-]无效ip:{}:{}'.format(ip, port))
#         else:
#             if res.status_code == 200:
#                 print('[+]有效ip:{}:{}'.format(ip, port))
#                 # Write the valid IP to a file
#                 with open('ipporxy.txt', 'a+') as f:
#                     f.write(ip + ':' + str(port) + '\n')
#         # Close the socket connection
#         s.close()
#     except Exception as e:
#         print('[-]无效ip:{}:{}'.format(ip, port))
#         print(e)

# Example usage:
ip_is_alive(('127.0.0.1', 80))
