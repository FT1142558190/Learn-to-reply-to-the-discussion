import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def get_answer(question):
    pass


# 提交答案
def share_answers(data):
    pass
# 初始化配置
VIDEO_ENABLE = True
WORK_ENABLE = True
EXAM_ENABLE = True
SHARE_ANSWER = True
TIME_INTERVAL = 5

# 启动Chrome浏览器
driver = webdriver.Edge

# 登录系统
driver.get('https://mooc1.chaoxing.com')
driver.find_element(By.ID, 'username').send_keys('138xxxxxxxx')
driver.find_element(By.ID, 'password').send_keys('mypassword')
driver.find_element(By.ID, 'login-btn').click()

# 等待页面加载
WebDriverWait(driver, 10).until(EC.title_contains("智慧树"))

# 获取任务列表
task_list = driver.find_elements(By.CSS_SELECTOR, '.task-item')

for task in task_list:
    # 处理视频任务
    if VIDEO_ENABLE and 'video-task' in task.get_attribute('class'):
        # 检查任务状态
        status = task.find_element(By.CSS_SELECTOR, '.task-status').text
        if '已完成' in status:
            continue

        # 播放视频
        task.find_element(By.CSS_SELECTOR, '.task-play').click()

        # 等待视频加载
        time.sleep(10)

        # 跳到结束
        driver.execute_script("arguments[0].currentTime = arguments[0].duration;")

        # 提交任务
        task.find_element(By.CSS_SELECTOR, '.task-submit').click()

    # 处理测验任务
    elif WORK_ENABLE and 'work-task' in task.get_attribute('class'):
        # 获取测验页面
        iframe = task.find_element(By.CSS_SELECTOR, 'iframe')
        driver.switch_to.frame(iframe)

        # 答题提交
        for question in driver.find_elements(By.CSS_SELECTOR, '.question-item'):
            # 获取答案
            answer = get_answer(question.text)
            choices = question.find_elements(By.CSS_SELECTOR, '.question-choice')
            for choice in choices:
                if choice.text == answer:
                    choice.click()
                    break

        if driver.find_element(By.ID, 'submit-btn').is_displayed():
            driver.find_element(By.ID, 'submit-btn').click()

        # 返回任务列表
        driver.switch_to.parent_frame()

        # 收录考试答案
    elif EXAM_ENABLE and 'share-task' in task.get_attribute('class'):
        # 收录答案
        answers = []

        for question in driver.find_elements(By.CSS_SELECTOR, '.question-item'):
            answer = get_answer(question.text)
            answers.append({
                'question': question.text,
                'answer': answer
            })



    # 等待下一任务
    time.sleep(TIME_INTERVAL)

# 关闭浏览器
driver.quit()


# 获取题目答案(连接题库或API)
