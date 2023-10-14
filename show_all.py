from selenium.webdriver.common.by import By
import login
import time

def show_all(driver):

    while True:
        try:
            look_more = driver.find_element(By.XPATH, './/*[@id="getMoreTopic"]')
            look_more.click()
            time.sleep(2)
        except:
            break
    print('down')
