# -*- coding:utf-8 -*-
#作者 ：Lyle.Li
#时间 :2019/10/14 16:58
#文件 :test_04.py

#输入某年某月某日，判断这一天是这一年的第几天？
import datetime
def get_daynum():
    year =input("请输入年份：")
    month =input("请输入月份：")
    day =input("请输入天：")

    date1 = datetime.date(year=int(year),month=int(month),day=int(day))
    date2 =datetime.date(year=int(year),month=1,day=1)
    return ((date1-date2).days+1)

if __name__=='__main__':
    print(get_daynum())