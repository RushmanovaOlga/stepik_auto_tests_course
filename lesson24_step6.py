from selenium import webdriver
import time

from selenium.webdriver.common.by import By
try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    link = "http://suninjuly.github.io/cats.html"
    browser.get(link)
    button = browser.find_element(By.ID, "button")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()