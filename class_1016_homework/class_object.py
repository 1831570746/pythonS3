# -*- coding:utf-8 -*-
#作者 ：Lyle.Li
#时间 :2019/11/8 9:04
#文件 :class_object.py

#python类的语法

class BoyFriend:
    #类属性
    height =175
    weight =130

    money ="500万"

    #类函数/类方法
    def cooking(self):   #会做饭
        print("男朋友要回做饭！")

    def earn(self):   #会挣钱
        print("男朋友月薪是3万")


#实例/对象 具体的一个例子

bf =BoyFriend()   #一个实例
print(bf)

bf.earn()     #调用一个实例里面的类方法
print(bf.cooking())



#实例具有类里面的所有属性和方法的使用权限


