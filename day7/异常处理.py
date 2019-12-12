# -*- coding:utf-8 -*-
#作者 ：Lyle.Li
#时间 :2019/11/7 10:04
#文件 :异常处理.py

try:
    fh =open("testfile.txt","w+",encoding="utf-8")
    fh.write("这是一个测试文件，用于测试异常！！")
except IOError:
    print("Error:没有找到文件或读取文件失败")

else:
    print("内容写入文件成功")
    fh.close()

