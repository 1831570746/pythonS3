# -*- coding:utf-8 -*-
'''
集合（set）是一个无序的不重复元素序列
可以使用大括号{}或者set（）函数创建集合
创建格式：
    parame={value01,value02,.....}
    或者
    set(value)
'''
# basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# print(basket)         #去重特性
# print('orange' in basket)     #验证元素是否在集合里面

#集合间运算
'''
a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)
print(a-b)      #集合a中包含而集合b中不包含的元素
print(a | b)    #a或b中包含所有的所有元素（并集）
print(a&b)      #a和b中同时包含的元素（交集）
print(a^b)      #同时不包含a和b的所有元素（反交集）
'''

shopping={"淘宝","京东","拼多多","唯品会"}
# shopping.add("天猫")     #添加某个元素到集合中
# print(shopping)
# shopping.update({"双十一","双十二"}) #添加
# print(shopping)

#remover移除元素
# shopping.remove("唯品会")
# print(shopping)

#discard移除集合中不存在的
shopping.discard("屠夫")     #
print(shopping)


