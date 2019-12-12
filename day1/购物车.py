# -*- coding:utf-8 -*-
#作者 ：Lyle.Li
#时间 :2019/9/12 15:25
#文件 :购物车.py
"""
购物车程序
数据结构：
goods=[
{"name":"电脑","price":1999},
{"name":"鼠标","price":10},
{"name":"游艇","price":20},
{"name":"美女","price":998},
......
]

功能要求：
基础要求：
1.启动程序后，输入用户名密码后，让用户输入工资，然后打印商品列表
2.允许用户根据商品编号购买商品
3.用户选择商品后，检测余额是否足够，够就直接扣款，不足需提醒用户
4.可以随时退出，退出时，打印已购买商品和余额
5.在用户使用过程中，关键输出，如余额，商品已加入购物车等信息，需高亮显示


扩展需求：
1.用户下一次登录后，输入用户名密码，直接回到上次的状态，即上次消费的余额什么的还是那些，再次登录可继续购买
2.允许查询之间的消费记录
"""

import  os

#商品列表
goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "IPAD", "price": 1998},
    {"name": "手机", "price": 998},
    {"name": "玩具", "price": 50},
    {"name": "教科书", "price": 100}
]

def is_shop(user):
    """
    判断用户是否已消费数据
    :param user:
    :return:
    """
    flg = False
    if os.path.exists(r"user_shop.txt"):
        with open(r"user_shop.txt",'r',encoding="utf-8") as f:
            for line in f:
                if line.find(user) !=-1:
                    flg = True
                    break

    else:
        with open(r"user_shop.txt","w",encoding="utf-8") as f:
            f.write("")

    return flg


def login():
    """
    用户登录
    :return:
    """
    err_cnt = 0
    suc_user = ''  #返回用户登录成功

    while err_cnt <3:
        user = input('输入用户名：')
        pwd = input('输入密码：')

        if user =="lyle" and pwd =='123':
            print("登录成功")
            suc_user = user
            break

        else:
            print("登录失败")

        err_cnt +=1

    else:
        print('登录次数失败已超过3次')
    return suc_user

def check_salary():
    """
    检查收入
    :return:
    """
    while True:
        salary =input('输入工资：')
        if salary.isdigit():
            break

        else:
            print('工资输入错误，请重新输入！')

    return int(salary)

def shop(user,salary):
    """
    用户购物
    """
    shop_cart = []   #购物车
    while True:
        print('--------商品列表--------')
        for index,value in enumerate(goods):
            print("商品编号：%s  商品名称：%s 商品价格:%s"%(index,value['name'],value['price']))

        choice = input("输入商品编号：---输入q退出购买")

        if choice.isdigit():
            choice = int(choice)
            if 0<=choice < len(goods):
                price =goods[choice]['price']
                if (salary-price)>0:         #判断余额是否大于0
                    salary = salary-price
                    shop_cart.append(goods[choice])
                    print('\033[1;32;40m购买商品编号:%s   购买商品名称:%s   购买商品价格:%s\033[0m'
                          % (choice, goods[choice]['name'], goods[choice]['price']))
                    print('\033[1;32;40m工资余额=%s\033[0m' % salary)

                else:
                    print('余额不足')
                    continue

            else:
                print('商品编号不存在！')

        elif choice =='q':
            print('\033[1;31;40m------本次购物退出------\033[0m')
            if len(shop_cart)>0:
                print('-----本次购买商品列表------')
                with open(r'user_shop.txt','a+',encoding='utf-8') as f:
                    f.write('user:%s\n'%user)
                    for value in shop_cart:
                        shop_info ='购买商品名称:%s|购买商品价格：%s'%(value['name'],value['price'])
                        print('\033[1;32;40m%s\033[0m'%shop_info)
                        f.write(shop_cart + "\n")
                    bal_info = '工资余额:%s' %salary
                    print('\033[1;32;40m%s\033[0m'%bal_info)
                    f.write(bal_info + "\n")

            break

def get_shop(user):
    """
    获取文件得到用户已消费数据
    :param user:
    :return:
    """
    flg = False
    resume_goods = []   #消费商品
    with open(r'user_shop.txt','r',encoding='utf-8') as f:
        for line in f :
            if line.find("购买") !=-1:
                shop_li = line.split("|")
                resume_goods.append([shop_li[0].split(":")[1].strip(),shop_li[1].split(":")[1].strip()])
            elif line.find("余额")!=-1:
                last_bal.append(line.split(":")[1].strip())

        print("\033[1;32;40m历史购物：%s\033[0m"%resume_goods)
        print("\033[1;32;40m还剩下余额：%s\033[0m"%last_bal[-1])

if __name__ =='__main__':
    user = login()
    if user!='':
        print('[]登录成功'.format(user))
        while True:
            action =input('输入c查询消费记录，输入b购买商品，输入q退出：')
            if action =='q':
                print('\033[1;31;40m---退出程序------\033[0m')
                get_shop(user)
                break

            elif action =="c":
                if is_shop(user):
                    print("---查询之前的消费记录---")
                    get_shop(user)
                else:
                    print("---查询之前无消费记录---")

            elif action=='b':
                if not is_shop(user):
                    salary = check_salary()
                else:
                    salary = int(last_bal[-1])
                print('您工资现有:',salary)
                shop(user,salary)
















