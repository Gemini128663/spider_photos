import requests
import json
import urllib.request
import os
from urllib.parse import quote
def getsougou(keyword, number):
    for i in range(0, int(number), 48):
        url = 'https://pic.sogou.com/pics?query='+quote(keyword) \
        +'&mode=1&start='+str(i)+'&reqType=ajax&reqFrom=result&tn=0'

        imgs = requests.get(url)#请求状态码，返回值为200
        jd = json.loads(imgs.text)#jd数据类型为字典
        jd = jd['items']  # 寻找键为items
        imgs_url = []
        for url in jd:
            imgs_url.append(url['pic_url'])
        m=i
        path = 'F:\\spider_photos\\'+keyword+'/'
        isExists=os.path.exists(path)
        if not isExists:
            os.makedirs(path)
            print("创建文件目录成功")
        else:
            pass
        
        for i in imgs_url:
            pathname = path + str(m) +'.jpg'
            try:
                urllib.request.urlretrieve(i, pathname)
            except:
                pass
            print("正在下载第:", m)
            m+=1
            print(pathname)


