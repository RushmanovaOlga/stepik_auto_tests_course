from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    elements = browser.find_elements(By.CSS_SELECTOR, ".form-control")
    for element in elements:
        element.send_keys("1")

    import os

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла

   
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")

    element.send_keys(file_path)


    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()