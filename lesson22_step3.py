from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select


try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    xx = browser.find_element(By.ID, "num1")
    x = int(xx.text)
    yy = browser.find_element(By.ID, "num2")
    y = int(yy.text)
    z = x + y
    z = str(z)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(z)



    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()