# -*- coding:utf-8 -*-
import time

# def deco(f):
#     def wrapper(a,b):
#         start_time = time.time()
#         f(a,b)
#         end_time = time.time()
#         execution_time = (end_time - start_time)*1000
#         print("time is %d ms" %execution_time )
#     return wrapper
#
# @deco
# def f(a,b):
#     print("be on")
#     time.sleep(1)
#     print("result is %d"%(a+b))
#
# # if __name__ == '__main__':
# f(3,4)

# user_status = False       #用户登录了就把这个改成True
#
# def login(func):         #把要执行的模块从这里传进来
#     def inner(*args,**kwargs):   #定义一层函数
#         user = "lyle"           #存储用户的信息
#         psd = "abc123"          #存储用户的信息
#         global  user_status   #全局变量
#
#         if user_status == False:
#             username = input("user:")
#             password = input("pasword:")
#
#             if username == user and  password==psd:
#                 print("welcome login.....")
#                 user_status = True
#
#             else:
#                 print("wrong username or password!")
#
#         if user_status == True:
#             func(*args,**kwargs)   #验证通过 就会调用相应的功能
#     return inner      #用户调用login时，只会返回inner的内存地址，下次再调用时加上（）才会执行inner函数
#
# def home():
#     print("---首页---")
#
# @login
# def america():
#     print("---欧美专区---")
#
#
# def japan():
#     print("---日韩专区---")
#
# @login
# def henan():
#     print("---河南专区---")
#
#
# home()
# america()
# henan('3p')


# def wrapper(func):
#     def result():
#         print('before')
#         func()
#
#         print('after')
#
#     return result()
#
# @wrapper
# def foo():
#     print('foo')
#
#
# def dict_check(func):
#     def wrapper(*args,**kwargs):
#         dict_obj:dict=args[0]
#         key = args[1]
#         if key in dict_obj.keys():
#             print("键已经存在")
#         else:
#             return  func(*args,**kwargs)
#
#     return wrapper
#
#
# class MyDict(dict):
#     @dict_check
#     def add(self,key,value):
#         self[key] = value
#
# d1=MyDict({'a':1,'b':2,'c':3})
# d1.add("a",4)
# print(d1)
# d1.add("d",4)
# print(d1)

import time

# def demo():
#     start_time=time.time()
#     time.sleep(2)
#     print("welcome sir")
#     stop_time=time.time()
#     print("运行时间%s"%(stop_time-start_time))
# demo()


def timmer(func_name):
    def inner():
        start_time =time.time()
        func_name()
        end_time=time.time()
        print("运行时间%s"%(end_time-start_time))

    return inner

@timmer            #>>>>相当于demo =timmer(demo)
def demo():
    time.sleep(2)
    print("welcome sir")

demo()