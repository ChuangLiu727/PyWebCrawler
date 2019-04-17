# coding=UTF-8
#https://explorer.nebulas.io/main/api/account?p=49
#https://explorer.nebulas.io/main/api/address/n1ooMb6A5gS9UJFr5rot1JgifzWxToESaSF
#合约账户的type为1
#最多400页

import requests
from bs4 import BeautifulSoup
import codecs
import urllib.request as urlrequest
import json
from requests.exceptions import ReadTimeout, ConnectionError, RequestException
import time
import random

DOWNLOAD_URL = 'https://explorer.nebulas.io/main/api/account?p='

def get_contract_address_witherror(num):
    url = DOWNLOAD_URL+str(num)
    print("requests from : " + url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
    
    
    #异常处理
    try:
        resp = requests.get(url, headers=headers)
        print('Sucessful')
        json_content = resp.json()
        addressList = json_content['data']['addressList']
        for address in addressList:
            if address['type'] == 0:
                continue
            else:
                print("No." + str(address['rank']) + " is contract")
                with open("address_list.txt", "a") as outputfile:
                    outputfile.write("{} {}\n".format(address['rank'], address['hash']))
        return num + 1
        
    except ReadTimeout: # 访问超时的错误
        print('Timeout')
        return num
    except ConnectionError: # 网络中断连接错误
        print('Connect error')
        return num
    except SysCallError: 
        print('SysCallError')
        return num

num = 40
while num <= 400:
    num = get_contract_address_witherror(num)
    time.sleep(random.randrange(1,10))
print('completed')

'''
#状态码判断
if resp.status_code == 200 :
    print('Sucessful')
#异常处理
try:
    resp = requests.get('http://httpbin.org/get', timeout=0.5)
    print(resp.status_code)
except ReadTimeout: # 访问超时的错误
    print('Timeout')
except ConnectionError: # 网络中断连接错误
    print('Connect error')
except SysCallError: # 父类错误
    print('Error')
'''


