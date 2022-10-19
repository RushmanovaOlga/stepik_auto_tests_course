import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/find_link_text")
link = browser.find_element(By.LINK_TEXT, "224592")
link.click()

time.sleep(30)
browser.quit()
