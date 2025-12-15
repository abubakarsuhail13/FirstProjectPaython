import unittest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import HtmlTestRunner


#Unit testcase in the python
class GoogleSearchNFT(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_google_NFT(self):
        self.driver.get("https://www.google.com")
        self.driver.find_element(By.NAME, "q").send_keys("Nexaforge Tech LTD")
        self.driver.find_element(By.NAME, "btnK").click()

    @classmethod
    def tearDownClass(cls):
        input("Press ENTER to close the browser...")
        cls.driver.quit()
        print("First Test automated successfully.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner
    (output='C:/Users/Dell/PycharmProjects/FirstProjectPaython/reports'))





#Simple testcase in python
# driver = webdriver.Chrome()
# driver.implicitly_wait(10)
# driver.maximize_window()
# driver.get("https://www.google.com")
#
# driver.find_element(By.NAME, "q").send_keys("Nexaforge Tech LTD")
# driver.implicitly_wait(10)
# driver.find_element(By.NAME, "btnK").click()
#
# input("Press the enter to close the window.")
# driver.quit()
# print("First Test automated successfully.")
#
