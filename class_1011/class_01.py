# -*- coding:utf-8 -*-
#作者 ：Lyle.Li
#时间 :2019/10/30 17:39
#文件 :class_01.py



#作业题:
#给定一个路径，请打印出所欲的路径（直至这个路径下没有目录为止）
#思路：递归函数
import os
for path in os.listdir(os.getcwd()):
    if os.path.isdir(path):
        os.listdir(os.path.join(os.getcwd(),path))
        print("{0}还需要做进一步处理".format(path))
    else:
        print(os.path.join(os.getcwd(),path))
