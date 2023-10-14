import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import login
import discuss_20
import show_all
url = "https://mooc1.chaoxing.com/bbscircle/grouptopic?courseId=235910389&clazzid=79701336&ut=s&enc=90a67793f734e58d373fa86574a1887c&cpi=307452615&openc=a3776f5607f020d466809ef7c526bd43"  # 注意！！！此处应打开学习通课程，返回旧版，复制网址到此处，每个人的都不一样！！！
driver=login.login()
time.sleep(2)
driver.get(url)
time.sleep(2)
handles = driver.window_handles
driver.switch_to.window(handles[-1])
time.sleep(2)
show_all.show_all(driver)
topics = driver.find_elements(By.CSS_SELECTOR, "[id^='topic_']")
discuss_20.discuss_for(topics,driver)


























print("结束了")