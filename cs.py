from selenium.webdriver.common.by import By
import login
import time
import discuss_20
import show_all
txt = ("请党放心，强国有我。")
url = "https://mooc1.chaoxing.com/bbscircle/grouptopic?courseId=235749144&clazzid=79401396&ut=s&enc=a9598f770ce81bcb13a81dab736f7fca&cpi=271545193&openc=7f92bdb7620e98e084fb08d2303ba8b6"  # 注意！！！此处应打开学习通课程，返回旧版，复制网址到此处，每个人的都不一样！！！
driver=login.login()
time.sleep(2)
driver.get(url)
time.sleep(2)
handles = driver.window_handles
driver.switch_to.window(handles[-1])
time.sleep(2)
topics = driver.find_elements(By.CSS_SELECTOR, "[id^='topic_']")
time.sleep(2)
show_all.show_all(driver)




time.sleep(30)
# 