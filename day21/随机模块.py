# -*- coding:utf-8 -*-
#作者 ：Lyle.Li
#时间 :2019/10/7 15:27
#文件 :随机模块.py



# def v_code():
#     ret = ''
#     for i in range(5):
#         num =random.randint(0,9)
#         alf = chr(random.randint(65,122))
#         s =str(random.choice([num,alf]))
#         ret+=s
#
#     return ret
# print(v_code())




# checkcode = ''
# for i in range(5):
#     current = random.randrange(0,5)
#     if current !=i:
#         temp = chr(random.randint(65,90))
#     else:
#         temp =random.randint(0,9)
#     checkcode+=str(temp)
#
# print(checkcode)
#
# print(random.randint(1,3))
# cc = chr(random.randrange(50,100))
# print(cc)
#
# list = random.randrange(0,99,3)
# print(list)
import random,time

code = ''
for i in range(4):
    temp = random.randrange(0,4)
    if temp!=i:
        temp=chr(random.randint(65,90))
    else:
        temp =random.randint(0,9)

    code+=str(temp)

print(code)














