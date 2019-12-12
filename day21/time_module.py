# -*- coding:utf-8 -*-
#作者 ：Lyle.Li
#时间 :2019/10/8 18:13
#文件 :time_module.py

# import time,sys
# print(time.process_time())   #返回处理器时间
# print(time.altzone)     #返回与utc时间的时间差，以秒计算
# print(time.asctime())   #返回时间格式Tue Oct  8 18:16:26 2019
# print(time.localtime())  #返回本地时间的struct_time对象格式
# print(time.asctime(time.localtime()))
#
#
# #将日期字符串转换成时间戳
# string_2_struct = time.strptime("2019/10/08","%Y/%m/%d")
# print(string_2_struct)
#
# string_2_stamp = time.mktime(string_2_struct)
# print(string_2_stamp)
#
# print(time.gmtime(time.time()-86640))
# print(time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime()))
#
# print(sys.version)


import time
# print(time.time())
#
# print(time.localtime())
# print(time.gmtime())
# print(time.strftime("%Y:%m:%d %X"))

true_time = time.mktime(time.strptime(''))








