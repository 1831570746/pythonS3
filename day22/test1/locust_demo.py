# -*- coding:utf-8 -*-
#作者 ：Lyle.Li
#时间 :2019/12/2 9:55
#文件 :locust_demo.py

import os

from locust import HttpLocust,TaskSet,task

class LocustDemo(TaskSet):
    @task(1)
    def baidu(self):
        req = self.client.get('/')
        if req.status_code==200:
            print("success")
        else:
            print("fail")

class WebsiteUser(HttpLocust):
    task_set = LocustDemo
    # wait_time =between(3,6)
    min_wait = 3000
    max_wait = 6000
if __name__=="__main__":
    os.system("locust -f locust_demo.py --host=https://www.baidu.com/")



