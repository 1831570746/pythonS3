# -*- coding:utf-8 -*-
#1、创建一个空列表，命名为names，往里面添加 Lihua、Rain、Jack、Xiuxiu、Peiqi和Black元素。
names =["Lihua","Rain","Jack","Xiuxiu","Peiqi","Black"]

#2、往(1)中的names列表里Black前面插入一个Blue。
names.insert(-1,"Blue")
print(names)

#3、把names列表中Xiuxiu的名字改成中文
names[3]="秀秀"
print(names)

#4、往names列表中Rain后面插入一个子列表["oldboy","oldgirl"]。
# names.insert(2,["oldboy","oldgirl"])
# print(names)

#5、返回names列表中Peiqi的索引值（下标）。
print(names.index("Peiqi"))

#6、创建新列表[1,2,3,4,2,5,6,2,]，合并到names列表中。
names_num=[1,2,3,4,2,5,6,2]
names.extend(names_num)
print(names)

#7、取出names列表中索引4-7的元素。
print(names[4:8])

#8、取出names列表中索引2-10的元素，步长为2。
print(names[2:11:2])

#9、取出names列表中最后3个元素。
print(names[-3:])

#10、循环names列表，打印每个元素的索引值和元素。
for i in names:

    print(names.index(i),i)

#11、循环names列表，打印每个元素的索引值和元素，当索引值为偶数时，把对应的元素改成-1
# for index,i in enumerate(names):
#
#     if index % 2 ==0:
#         names[index]=-1
#         print(index,i)
# print(names)

#12、names列表里有3个2，请返回第二个2的索引值，不要人肉，要动态找。
"""
13、现有商品列表如下：
　　products =   [["iphone",6888],["MacPro",14800],["小米6",2499],["Coffee",31],["Book",60],["Nike",699]]，需打印出以下格式：
"""
# products =[["iphone",6888],["MacPro",14800],["小米6",2499],["Coffee",31],["Book",60],["Nike",699]]
# print("-------商品列表-------")
# for index,i in enumerate(products):
#     print("%s %s    %s"%(index,i[0],i[1]))

#14、根据（13）里的products列表写一个循环，不断询问用户想买什么，用户选择一个商品编号，就把对应的商品添加到购物车里，最终用户输入q退出时，打印购买的商品列表。

products =[["iphone",6888],["MacPro",14800],["小米6",2499],["Coffee",31],["Book",60],["Nike",699]]
# print("-------商品列表-------")
# for index,i in enumerate(products):
#     print("%s %s    %s"%(index,i[0],i[1]))

shop_car = []   #用户购物车
shop_cost = 0    #用户花费的金额
exit_log = False
while not exit_log:
    print("------------商品列表------------")
    for index ,i in enumerate(products):
        print("%s %s    %s" % (index, i[0], i[1]))
    user_choice=input("\n 输入你想购买的产品序号（按“q”退出）：")
    if user_choice.isdigit():
        user_choice =int(user_choice)
        if user_choice>=0 and user_choice<len(products):
            #判断用户购买的商品是否在商品列表中
            shop_car.append(products[user_choice])      #加入购物车
            shop_car += products[user_choice][1]        #计算费用
            print("\n %s 已经加入你的购物车\n"%products[user_choice])

        else:
            print("抱歉，此商品不存在\n")
    elif user_choice =="q":
        #用户选择退出
        if len(shop_car)>0:
            print("\n---------你的购物车---------")
            for index,i in enumerate(shop_car):
                print("%s %s"%(i[0],i[1]))

            print("\n你的此次购物的花费合计是：%s元\n"%shop_cost)
            exit_log=True

        else:
            exit_log =True

    else:
        #输入不合法
        exit_log =True
