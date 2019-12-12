# -*- coding:utf-8 -*-
#作者 ：Lyle.Li
#时间 :2019/12/2 18:04
#文件 :Baidu_demo.py
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver =webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://uums.whgxwl.com:6060/auth/login")

def Loggin(username,password):
    driver.find_element_by_id("username").clear()
    driver.find_element_by_id("username").send_keys(username)
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_xpath("//button[@class='ant-btn ant-btn-primary ant-btn-lg ant-btn-block']").click()
    driver.find_element_by_xpath("//button[@class='ErpBtn ant-btn ant-btn-default ant-btn-circle']").click()


Loggin(u'fs_product_test',u'11111111')


