# coding=UTF-8
#https://explorer.nebulas.io/main/api/account?p=49
#https://explorer.nebulas.io/main/api/address/n1ooMb6A5gS9UJFr5rot1JgifzWxToESaSF
#合约账户的type为1
#最多400页

import pandas as pd
import requests
import time
from bs4 import BeautifulSoup
import codecs
import urllib.request as urlrequest
import json
from requests.exceptions import ReadTimeout, ConnectionError, RequestException
import random
DOWNLOAD_URL = 'https://explorer.nebulas.io/main/api/address/'

def get_contract_witherror(address):
    url = DOWNLOAD_URL + address
    print("requests from : " + url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
    #异常处理
    try:
        resp = requests.get(url, headers=headers)
        print('Sucessful')
        json_content = resp.json()
        contractCode = json_content['data']['contractCode']
        jsoncontractCode = json.loads(contractCode)
        contractCode = jsoncontractCode['Source']
        print("Save contract in : contract/" +address+".js")
        with open("contract/"+address+".js", "a") as outputfile:
            outputfile.write("{}\n".format(contractCode))
        return True
        
    except ReadTimeout: # 访问超时的错误
        print('Timeout')
        return False
    except ConnectionError: # 网络中断连接错误
        print('Connect error')
        return False

# 获取address list
data = pd.read_table('address_list.txt',header=None,encoding='gb2312',delim_whitespace=True,index_col=0)
col=data.iloc[:,0]
arrs=col.values
#print(arrs)
print(len(arrs))

# 爬取
i = 0
while i< len(arrs):
    if get_contract_witherror(arrs[i]):
        i = i + 1
    else:
        pass
    time.sleep(random.randrange(1,10))