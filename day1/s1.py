# -*- coding:utf-8 -*-
#列表去重特性
# number={1,2,3,4,5,5,6,7}
# print(number)
#
# data = 0.87246
# print("%.2f%%" % (data * 100))          #百分数
#
# demo = 0.62315
# print("%.2f%%"%(demo*100))

# def formatSize(bytes):
#     try:
#         bytes=float(bytes)
#         kb = bytes/1024
#     except:
#         print("格式不对")
#         return "Error data"
#     if kb >=1024:
#         M = kb/1024
#         if M >= 1024:
#             G = M/1024
#             return "%fG"%(G)
#         else:
#             return "%fM"%(M)
#
#     else:
#         return "%fkb"%(kb)
#
# c=formatSize(1024)
# print(c)

# print(abs(-10))         #求绝对值
# print(round(1.234))      #四舍五入
#
# print(pow(2,3))    #2的3次方

# for i in range(1,11):
#     if i ==7:
#         pass
#     else:
#         print(i,end=' ')
#
# s = 0
# for v in range(1,101):
#
#     s = s + v
#     v+=1
# print(s)
#
# n = 1
# while n<101:
#     temp = n % 2
#     if temp ==1:
#         print(n,end=' ')
#
#     else:
#         pass
#     n+=1
#
#
# q = 1
# while q<101:
#     temp = q % 2
#     if temp == 0:
#         print(q,end=' ')
#     else:
#         pass
#     q+=1

# count = 0
# while count<3:
#     user =input('>>>>')
#     pwd = input('>>>>')
#     if user == 'alex' and pwd == '123':
#         print('欢迎登陆')
#         break
#
#     else:
#         print('用户名或密码错误')
#     count = count+1

#
# sum = 0
# for i  in range(1,101):
#     sum = sum + i
#     i+=1
#
# print("1到100的和为：%d"%sum)

# list=[1,2,3,4]
# it = iter(list)    #创建迭代器对象
#
# for x in it:
#     print(x,end=' ')

# import sys      #引入sys模块
#
# list=[1,2,3,4]
# it = iter(list)   #创建迭代器对象
#
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()





#在20次迭代后停止执行
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a+=1
            return x
        else:
            raise StopIteration

myclass =MyNumbers()
myiter= iter(myclass)
for i in myiter:
    print(i,end=" ")
















