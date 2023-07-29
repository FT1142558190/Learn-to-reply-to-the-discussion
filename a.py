'''
Data：2020/6/11
--- 大威锅 | DaWeiGuo ---
'''
#代码没有实现翻翻页功能，大家可以自己改善啦，回复的就是讨论区当前页面的最新的20个话题
from selenium import webdriver#导入库
import time
from selenium.webdriver.common.by import By
username = ''
password = ''#你的密码

def reply(url):#回复函数
    browser.get(url)
    a = browser.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div[1]/p[2]/a[2]")
    a.click()
    text = browser.find_element(By.XPATH,"//textarea[@class='hfInp fl']")
    text.send_keys('111')#你要回复的内容
    tag = browser.find_element(By.XPATH,"//input[@class='fl grenBtn']")
    tag.click()


browser = webdriver.Edge#声明浏览器

url = 'https://mooc1.chaoxing.com/bbscircle/grouptopic?courseId=231380174&clazzid=69502047&ut=s&enc=e2cd760ddc7b255784c925a37fc9fa8a&cpi=304011130&openc=9b3d3630cafff19e6981fba9bb27dccd'#你要刷的课程讨论区的链接


browser.get('http://i.chaoxing.com')
browser.find_element(By.XPATH,"//input[@id='unameId']").send_keys(username)
browser.find_element(By.XPATH,"//input[@id='passwordId']").send_keys(password)
time.sleep(5)
browser.get(url)#打开浏览器预设网址
print('---Login---')
# print(browser.title)

reply_urls = browser.find_elements(By.XPATH,"//p[@class='stuFont ol']")#提取当前页面所有话题的讨论链接
# a = reply_url[0].find_element_by_tag_name('a').get_attribute('href')
# print(a)
url_list=[]
for reply_url in reply_urls:#放入列表
    li = reply_url.find_element(By.TAG_NAME,'a').get_attribute('href')
    url_list.append(li)

for i in range(len(url_list)):
    reply(url_list[i])#调用回复函数
    time.sleep(2)

# browser.get(url_list[0])
# a = browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[1]/p[2]/a[2]")
# a.click()
# text = browser.find_element_by_xpath("//textarea[@class='hfInp fl']")
# text.send_keys('111')
# tag = browser.find_element_by_xpath("//input[@class='fl grenBtn']")
# tag.click()

print('---End---')