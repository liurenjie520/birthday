import datetime
import json
import os
import requests
import urllib





def yujin():
    headers = {
        "Host": "www.iamwawa.cn",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Cookie": "PHPSESSID=d41i5vvp52a119knuokqk2ilh0; Hm_lpvt_ca368c21c1d2aa60e6f63d598c4cb02a=1624081986"
    }
    url = "https://www.iamwawa.cn/nongli/api"
    year = datetime.datetime.today().year
    year = str(year)
    params = {
        'type': 'lunar',
        'year': year,
        'month': 11,
        'day': 22
    }

    r = requests.post(url, headers=headers, data=params)
    js = json.loads(r.text)
    print(js)
    save_str = js["data"]["solar"]
    a1=save_str.replace('年', '')
    a2=a1.replace('月', '')
    a3=a2.replace('日', '')
    # print(type(save_str))
    print(a3)
    return a3

if __name__ == '__main__':
    print(yujin())
