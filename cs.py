#!/usr/bin/python
# -*- coding:utf-8 -*-
# author: vhow  python3
'''
注意！！！
本代码在chrome浏览器上自动测试
运行此代码需要selenium库和chromedriver
chromedriver版本为chrome的版本
本代码用的版本是 87.0.4280.88
通过下面的链接下载和你chrome版本相同的driver并放置于python.exe所在同级文件夹下
http://npm.taobao.org/mirrors/chromedriver/
代码跑起来后可最小化后台运行，或者开启静默模式不显示浏览器
'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime
import json
from selenium.common.exceptions import StaleElementReferenceException

import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

# 输入账号
student_id ="1asd0703"#input("手机号:")
# 输入密码
password = "dasd"#input("密码:")
url = "https://mooc1.chaoxing.com/bbscircle/grouptopic?courseId=235749144&clazzid=79401396&ut=s&enc=a9598f770ce81bcb13a81dab736f7fca&cpi=271545193&openc=7f92bdb7620e98e084fb08d2303ba8b6"#注意！！！此处应打开学习通课程，返回旧版，复制网址到此处，每个人的都不一样！！！
#自定义讨论内容
tl1 = ("请党放心，强国有我。")
# tl2 = ("如何超链接应用与制作帮助信息页面")
# tl3 = ("如何表格应用与制作购物车页面")
# tl4 = ("如何表单应用与制作注册登录页面")
# tl5 = ("如何网页布局与制作商品筛选页面")
# tl6 = ("如何模板应用与制作商品推荐页面")
# tl7 = ("如何网页特效与制作商品详情页面")
# tl8 = ("如何网站整合与制作购物网站首页")
# tl9 = ("如何搭建ASP.NET网站的运行与开发环境")
# tl10 = ("如何使用控件高效创建网站页面")
# tl11 = ("如何取用客户端和服务器的信息")
# tl12 = ("如何控制网站页面的外观")
# tl13 = ("如何快速实现网站的导航")
# tl14 = ("如何新建商品目录")
# tl15 = ("如何使用ADO.NET获取与处理数据")
# tl16 = ("如何使用LINQ集成查询与更新数据")
# tl17 = ("如何应用I0和流操纵文件和图片")
# tl18 = ("如何整合与发布网站")
# tl19 = ("三相异步电动机如何实现点动和自锁")
# tl20 = ("举例说明PLC控制电机正反转在现实生活的应用")

# 打开chrome浏览器
driver = webdriver.Edge()
# get请求网址
driver.get('http://i.chaoxing.com')
# 浏览器最大化 一定需要，否则会影响后面元素定位
driver.maximize_window()
# 设置浏览器大小
driver.set_window_size(1200, 700)
#以下是简单的
student_num = driver.find_element(By.XPATH,'//*[@id="phone"]')
student_num.send_keys(student_id)
student_pwd = driver.find_element(By.XPATH,'//*[@id="pwd"]')
student_pwd.send_keys(password)

driver.find_element(By.XPATH,'//*[@id="loginBtn"]').click()
#给1秒等待加载时间，以下不在详述
time.sleep(1)
#访问到讨论网址
driver.get(url)
time.sleep(1)

handles = driver.window_handles
driver.switch_to.window(handles[-1])
#//*[@id="reply_count_482006684"]
time.sleep(1)

topics = driver.find_elements(By.CSS_SELECTOR, "[id^='topic_']")

for topic in topics:

    reply_btn = topic.find_element(By.XPATH, './/div / div[1] / div[2]')
    reply_btn.click()
    time.sleep(1.5)
    handles = driver.window_handles
    driver.switch_to.window(handles[-1])
    a = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[1]/div[1]/p[2]/a[2]')
    a.click()
    reply_input = driver.find_element(By.TAG_NAME, "textarea")
    reply_input.clear()
    reply_input.send_keys(tl1)
    time.sleep(0.5)
    reply_btn = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[4]/div[1]/input')
    reply_btn.click()
    time.sleep(1.5)
    dian=driver.find_element(By.XPATH,'/ html / body / div[2] / div[2] / div[2] / div[1] / div / div[1] / a[2]')
    dian.click()
    time.sleep(0.5)
    driver.close()
    time.sleep(0.5)
    handles = driver.window_handles
    driver.switch_to.window(handles[-1])
print("结束了")