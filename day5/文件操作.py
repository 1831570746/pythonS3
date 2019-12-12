# -*- coding:utf-8 -*-
# from sys import argv
# script,filename = argv
# f = open(filename)
# print("Here's your file %r:"%filename)
# print(f.read())
# print("Type the filename again:")
# file_again =input(">>>>")
# txt_again = open(file_again)
# print(txt_again.read())


with open('test.txt','a',encoding="utf-8") as  file_test:
    file_test.write('浩哥是个美男子！\n')
    file_test.write('请关注浩哥哟！\n')



with open('test.txt','r',encoding="utf-8") as  file_test:
    str = file_test.read()
    print(str)












