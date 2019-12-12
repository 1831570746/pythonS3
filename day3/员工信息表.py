# -*- coding:utf-8 -*-
#作者 ：Lyle.Li
#时间 :2019/9/26 17:13
#文件 :员工信息表.py
"""python员工信息表操作"""
import sys
import os

def select1():
    with open('peopledb','r',encoding="utf-8") as f:
        line = f.readlines()
        for i in line:
            print(i)

def select():
    msg = '''
    请输入或复制查询命令例如：

    　   1. select name,age from staff_table where age > 22
　　     2. select * from staff_table where dept = "IT"
        3. select * from staff_table where enroll_date like "2013"
    '''
    print(msg)
    user_choice_input = input(">>>:")
    user_choice_input1=user_choice_input.split(' ')
    if user_choice_input=='select name,age from staff_table where age >%s'%(user_choice_input1[7]):
        with open('peopledb','r+',encoding='utf-8') as f:
            list1=[]
            count = 0
            for line in f:
                i =line.strip().split(',')
                if i[2] > user_choice_input1[7]:
                    list1.append(i)

            for s in list1:
                count+=1






