# -*- coding:utf-8 -*-
lst=["肖申克救赎","战狼","绿皮书","大黄蜂","斗鱼"]
#索引
# print(lst[2])
#print(lst.index("绿皮书"))  #通过索引返回元素的位置

#切片
# print(lst[1::2])          #从列表中1到最后 步长是2 取值
#
# print(lst[-3:-1])


#增加
# lst.append("沙克")
# print(lst)

#删除
# lst.pop()     #删除列表中最后一个元素
# print(lst)

# lst.remove("绿皮书")       #删除列表中指定的一个元素
# print(lst)

#修改
# lst.insert(-4,"Lol")
# print(lst)

# lst[2]="七个小矮人"      #指定某个元素进行更改
# print(lst)


# lst[1::2]=("天使的翅膀","降魔杵")   #指定某个元素 步长为2
# print(lst)


# bicycles = ['trek','cannondale','redline','specialized']
# print(bicycles)
# print(bicycles[0].title())
# print(bicycles[-1])
# bicycles[1] ='ducati'
# print(bicycles)

products =[["iphone",6888],["MacPro",14800],["小米6",2499],["Coffee",31],["Book",60],["Nike",699]]

for index,i in enumerate(products):
    print("%s %s"%(index,i))





