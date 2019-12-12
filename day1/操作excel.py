# -*- coding:utf-8 -*-
#只能写不能读
import xlwt
stus = [['姓名','年龄','性别','分数'],
        ['mary',20,'女',89.9],
        ['rose',22,'女',89.6],
        ['jack',21,'男',89.5],
        ['xixi',23,'女',90.0]
        ]
book = xlwt.Workbook()  #新建一个Excel
sheet = book.add_sheet('casel_sheet')  #添加一个sheet页
row = 0                #控制行
for stu in stus:
    col = 0            #控制列
    for s in stu:       #在循环里面list的值，每一列
        sheet.write(row,col,s)
        col+=1
    row+=1

book.save('stu_1.xls')    #保存到当前目录下























