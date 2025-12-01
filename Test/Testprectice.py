import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# driver = webdriver.Edge()
# driver.get("http://www.google.org")
driver.maximize_window()
driver.set_page_load_timeout(20)
driver.get("http://www.nexaforgetech.com")
#driver.find_element(By.NAME, "q").send_keys("NexaForge Technologies")
#driver.find_element(By.NAME, "btnK").click()

time.sleep(3)
driver.quit()
