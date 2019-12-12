# -*- coding:utf-8 -*-
#作者 ：Lyle.Li
#时间 :2019/10/7 11:18
#文件 :函数.py

# def chi(*food):    #在形参这里把传递过来的实参进行聚合，聚合成了元组
#     print(food)
#
# chi("小米粥")
# chi("小米粥","咸鸭蛋")
#
#
#
#
# def func(*args,a,b,c):
#     print(a,b,c,args)
#
# func(1,2,3,4,5,6,7,a=8,b=9,c=10)

# def log(func):
#     def warapper(*args,**kwargs):
#         print('call %s():'%func.__name__)
#         return func(*args,**kwargs)
#     return warapper
# @log
# def now():
#     print('2019-10-01')
# now()

# import functools
#
# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args,**kwargs):
#         print('call %s():'%func.__name__)
#         return func(*args,**kwargs)
#     return wrapper
#
# @log
# def now():
#     print('2019-10-07')
# now()
#
# def logger(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args,**kw):
#             print('%s %s():'%(text,func.__name__))
#             return func(*args,**kw)
#         return wrapper
#     return decorator
#
# @logger
# def today():
#     print('2019-10-07')
#
# today()
#
# print(today.__name__)


# def hello():
#     print('你好，python')
#
# def tpl_sum(T):
#     result = 0
#     for i in T:
#         result+=i
#     return result


import requests
url ="https://passport.cnblogs.com/user/LoginInfo"
headers ={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}

s = requests.session()
r = s.get(url,headers=headers,verify=False)
print(s.cookies)

c =requests.cookies.RequestsCookieJar()
c.set('.Cnblogs.AspNetCore.Cookies','CfDJ8DeHXSeUWr9KtnvAGu7_dX9tx3aAT7SDv8Y-Q1ozho6XIrLbpDN3XemVboULgDbVkvHJNxcBxp8tBTGQbAA9umos3ZUpFoMkBZpUUZlwhHQ8obPQlMrce69Zx1Ca6-UnQFCEUg7Y1vvY2ivUXu3saO1aieMoDbuP3uTrBUnJ_5obVDU1ZKPj8zlTBxuF05C9ZhqmLZgg4FFcmAELlrw_66HOVBK4wfoCHpD_UJhFow4xDQR5_0R4V1sXVxDVyxJ0kEhnN8TQAw7JZL8xAqrQCQbn4GayuQeTAzFAkwC3NNGJw4xgLDT5RUUwwPKJrb6SwIqve-WHx37Dvz9Sexj6XdS_BFLKR3yhl7mrev42yzfJL4KtbPCrHJhJf5mYa5yxDkCyoETI0eMMKjPm65xw9vdqIXBIfzFKvAd-X4EcmiuWvCPggnc7Zqo_l18OFRWGvwWD3-ET9MN2a_ZRvOSWHhk')
c.set('.CNBlogsCookie',"39F25C65410D52CFF4F05C1EFBAC1E5229372712D06EF538D06672266440277041615B590A29D5242BE0FACD0C4A858AB40907410EC49464FE621CE18CCC67466BACA1D09CD3F3297D6DBBB923F7422147B13B4A")

s.cookies.update(c)
print(s.cookies)

#登录成功后保存编辑内容
r1 =s.get("https://i.cnblogs.com/EditPosts.aspx?opt=1",headers=headers,verify=False)


#保存草稿箱
url2="https://i.cnblogs.com/EditPosts.aspx?opt=1 "
body={
    "__VIEWSTATE":"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",
    "__VIEWSTATEGENERATOR":"FE27D343",
    "Editor$Edit$txbTitle":"测试123",
    "Editor$Edit$EditorBody":"<p>这是IEhao的博客园</p>",
    "Editor$Edit$Advanced$ckbPublished":"on",
    "Editor$Edit$Advanced$chkDisplayHomePage":"on",
    "Editor$Edit$Advanced$chkComments":"on",
    "Editor$Edit$Advanced$chkMainSyndication":"on",
    "Editor$Edit$Advanced$txbEntryName":"",
    "Editor$Edit$Advanced$txbExcerpt":"",
    "Editor$Edit$Advanced$txbTag":"",
    "Editor$Edit$Advanced$tbEnryPassword":"",
    "Editor$Edit$lkbDraft":"存为草稿",
}


r2 =s.post(url2,data =body,verify=False)
print(r.content)