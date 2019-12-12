# -*- coding:utf-8 -*-
#作者 ：Lyle.Li
#时间 :2019/10/25 15:11
#文件 :sys_module.py


# print(sys.argv)

# print(sys.version)   #获取python解释程序的版本信息
import sys
import time

#============实现打印进度条函数=================
def progress(percent,width=50):
    if percent>=1:
        percent=1
    show_str =('[%%-%ds]'%width) %(int(width*percent)*'#')
    print('\r%s %d%%'%(show_str,int(100*percent)),file=sys.stdout,flush=True,end='')


#----------应用------------
data_size =1025
recv_size =0
while recv_size<data_size:
    time.sleep(1.5)
    recv_size+=1024

    percent=recv_size/data_size
    progress(percent,width=70)


