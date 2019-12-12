# -*- coding:utf-8 -*-
#作者 ：Lyle.Li
#时间 :2019/10/14 16:33
#文件 :test_03.py

import math
def fun():
    for i in range(-100,10000):
        x=math.sqrt(i+100)%1
        y=math.sqrt(i+268)%1
        if x==0 and y==0:
            print(i)

fun()







