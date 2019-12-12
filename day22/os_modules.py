# -*- coding:utf-8 -*-
#作者 ：Lyle.Li
#时间 :2019/10/25 12:04
#文件 :os_modules.py

import os

# print(os.getcwd())  #获取当前目录下的路径

# os.chdir('test1') #改变当前目录下的路径，相当于linux中的cd命令
# print(os.getcwd())

# os.makedirs('dirname1/dirname2')   #生成多层递归目录

# os.removedirs('dirname1/dirname2')    #删除多级目录

# os.mkdir('dirname')   #生成单级目录


# os.rmdir('dirname')    #删除单级空目录

# print(os.listdir('test1'))   #列出指定目录下的所有文件和子目录

# os.remove('test1/ssss.py')   #删除指定目录下的文件

# os.rename("test1/sss.py","ssss.py")     #重命名文件/目录

# print(os.stat('ssss.py'))   #获取文件相关信息   st_size：文件大小   st_atime:最近存取时间  st_mtime:最近修改时间    st_ctime:最后权限修改时间

# print(os.name)  #指出当前使用平台

# os.system("bash command")   #运行shell命令，直接显示

# print(os.path.abspath("D:/test/pythonS3/day22/os_modules.py"))    #返回path规范化的绝对路径

# print(os.path.split("D:/test/pythonS3/day22/os_modules.py"))      #将path分割成目录和文件名二元组返回

# print(os.path.dirname("D:/test/pythonS3/day22/os_modules.py"))      #返回path的目录

# print(os.path.basename("D:/test/pythonS3/day22/os_modules.py"))      #返回path最后的文件名

# print(os.path.split("D:/test/pythonS3/day22/os_modules.py")[1])   #取出第二个元素

# print(os.path.getatime("D:/test/pythonS3/day22/os_modules.py"))     #返回path所指向的文件或者目录的最后存取时间

# print(os.path.getmtime("D:/test/pythonS3/day22/os_modules.py"))      #返回path所指向的文件或者目录的最后修改时间

# print(os.path.getsize("D:/test/pythonS3/day22/os_modules.py"))     #返回path的文件大小



import os,sys
possible_topdir =os.path.normpath(os.path.join(
    os.path.abspath(__file__),
    os.pardir,
    os.pardir,
    os.pardir
))
print(sys.path.insert(0,possible_topdir))