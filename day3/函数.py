# -*- coding:utf-8 -*-
#作者 ：Lyle.Li
#时间 :2019/9/26 16:37
#文件 :函数.py

#语法定义
# def sayhi():    #函数名
#     print("hello, I'm nobody!")
#
# sayhi()   #调用函数
#
# #函数带参数
# a,b = 5,8
# c=a**b
# print(c)
#
# def clac(x,y):
#     res = x**y
#     return res
# # c=clac(a,b)
# # print(c)
# print(clac(5,8))

def stu_register(name,age,course,country="CN"):
    print("-----注册学生信息-----")
    print("姓名:",name)
    print("age:",age)
    print("国籍:",country)
    print("课程:",course)

stu_register("刘老根","21","Java")




















