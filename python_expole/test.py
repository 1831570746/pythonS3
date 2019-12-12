# -*- coding:utf-8 -*-
#作者 ：Lyle.Li
#时间 :2019/9/20 16:45
#文件 :test.py


#题目：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数
def test_01():
    count = 0
    num_lst =[]
    for i in range(1,5):
        for j in range(1,5):
            for k in range(1,5):
                if (i!=j) & (j!=k) and(i!=k):
                    count+=1
                    print("%d%d%d"%(i,j,k))
                    num_lst.append((i,j,k))
    return num_lst
test_01()








