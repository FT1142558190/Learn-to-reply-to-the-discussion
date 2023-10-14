import time
from selenium import webdriver
from selenium.webdriver.common.by import By
def discuss_for(topics,driver):
    if len(topics)==1:
        while(True):
            reply_btn = topics[0].find_element(By.XPATH, './/div / div[1] / div[2]')
            reply_btn.click()
            time.sleep(1.5)
            handles = driver.window_handles
            driver.switch_to.window(handles[-1])
            String_text = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div/h3")
            txt = String_text.text
            a = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[1]/p[2]/a[2]')
            a.click()

            reply_input = driver.find_element(By.TAG_NAME, "textarea")
            reply_input.clear()
            reply_input.send_keys(txt)
            time.sleep(0.5)
            reply_btn = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[4]/div[1]/input')
            reply_btn.click()
            time.sleep(1.5)
            dian = driver.find_element(By.XPATH,
                                       '/ html / body / div[2] / div[2] / div[2] / div[1] / div / div[1] / a[2]')
            dian.click()
            time.sleep(0.5)
            driver.close()
            time.sleep(0.5)
            handles = driver.window_handles
            driver.switch_to.window(handles[-1])
    else:
        for topic in topics:
            reply_btn = topic.find_element(By.XPATH, './/div / div[1] / div[2]')
            reply_btn.click()
            time.sleep(1.5)
            handles = driver.window_handles
            driver.switch_to.window(handles[-1])
            String_text = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div/h3")
            txt = String_text.text
            a = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[1]/p[2]/a[2]')
            a.click()

            reply_input = driver.find_element(By.TAG_NAME, "textarea")
            reply_input.clear()
            reply_input.send_keys(txt)
            time.sleep(0.5)
            reply_btn = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[4]/div[1]/input')
            reply_btn.click()
            time.sleep(1.5)
            dian = driver.find_element(By.XPATH,
                                       '/ html / body / div[2] / div[2] / div[2] / div[1] / div / div[1] / a[2]')
            dian.click()
            time.sleep(0.5)
            driver.close()
            time.sleep(0.5)
            handles = driver.window_handles
            driver.switch_to.window(handles[-1])
