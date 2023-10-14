import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def login():
    student_id = '''15192860703
    '''  # input("手机号:")
    # 输入密码
    password = '''
    dsc770556'''  # input("密码:")
    # 自定义讨论内容


    # 打开chrome浏览器
    driver = webdriver.Edge()
    # get请求网址
    driver.get('http://i.chaoxing.com')
    # 浏览器最大化 一定需要，否则会影响后面元素定位
    driver.maximize_window()
    # 设置浏览器大小
    driver.set_window_size(1200, 700)
    # 以下是简单的
    student_num = driver.find_element(By.XPATH, '//*[@id="phone"]')
    student_num.send_keys(student_id)
    student_pwd = driver.find_element(By.XPATH, '//*[@id="pwd"]')
    student_pwd.send_keys(password)

    driver.find_element(By.XPATH, '//*[@id="loginBtn"]').click()
    # 给1秒等待加载时间，以下不在详述
    time.sleep(1)
    return driver