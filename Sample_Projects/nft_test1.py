import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import HtmlTestRunner  # Make sure this matches your installed package

class GoogleSearchNFT(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_google_NFT(self):
        self.driver.get("https://www.google.com")
        search_box = self.driver.find_element(By.NAME, "q")
        search_box.send_keys("Nexaforge Tech LTD" + Keys.ENTER)

    @classmethod
    def tearDownClass(cls):
        input("Press ENTER to close the browser...")
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))
