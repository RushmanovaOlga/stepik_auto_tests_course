from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()



    x_element = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
    x = x_element.text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    answer = browser.find_element(By.ID, "answer")



    y = calc(x)

    answer.send_keys(y)


    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()




finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()