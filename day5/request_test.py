# -*- coding:utf-8 -*-
#作者 ：Lyle.Li
#时间 :2019/10/11 17:12
#文件 :request_test.py

import requests,json
url = "http://www.kuaidi.com/index-ajaxselectcourierinfo-773007742967132-shentong.html "
headers={
    "User-Agent":"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}
s = requests.session()
r= s.get(url,headers=headers,verify=False)
result = r.json()
data =result["data"]   #获取data里面内容
print(data)
print(data[0])         #获取data最上面
get_result = data[0]['context']        #获取已签收状态
print(get_result)

if u"已签收" in get_result:
    print("快递单已签收成功")
else:
    print("未签收")