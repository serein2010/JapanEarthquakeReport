import json
import os
import urllib.request
import time
url="https://api.wolfx.jp/jma_eew.json"
dir=os.getcwd()
while True:
    urllib.request.urlretrieve(url, dir+'\data\json\eq.json')
    print('下载完成')
    time.sleep(3)
