# -*- coding:utf-8 -*-

#字典是一种可变容器模型，且可储存任意类型对象
    #字典的每个键值 key=>value 对用冒号 : 分割，每个键值对之间用逗号 , 分割，整个字典包括在花括号 {} 中

# dict={'a':1,'b':2,'c':3,'d':4}
#
# print(dict['b'])


dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

#修改字典
    #向字典添加新内容的方法是增加新的键/值对
'''
dict['Age']=8   #更新
dict['School']="Niubi"   #添加

print("dict['Age']:",dict['Age'])
print("dict['School']:",dict['School'])
print(dict)
'''

#删除字典

# del dict['Name']
# print(dict)

dict1 = {'Name': 'Zara', 'Age': 7}
# dict2 = {'Name': 'Mahnaz', 'Age': 27}
# dict3 = {'Name': 'Abid', 'Age': 27}
# dict4 = {'Name': 'Zara', 'Age': 7}
# print("Return Value : %d" % cmp (dict1, dict2))
# print("Return Value : %d" % cmp (dict2, dict3))
# print("Return Value : %d" % cmp (dict1, dict4))
print(len(dict1))    #计算字典元素个数
print(str(dict1))     #输出字典 打印出字典格式














