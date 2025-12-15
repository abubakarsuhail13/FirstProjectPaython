import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.set_page_load_timeout(20)
driver.get("http://www.nexaforgetech.com")

# Wait for the element and then click it
element = (WebDriverWait(driver, 10).until
           (EC.visibility_of_element_located((By.LINK_TEXT, "Let's Build Together"))))
element.click()
print("This case successfully executed!")

time.sleep(3)
driver.quit()
