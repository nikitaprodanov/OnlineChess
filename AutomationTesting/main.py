import unittest
from selenium import webdriver
import time

class BasicOnlineChessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("./chromedriver")
        self.driver.get("http://127.0.0.1:5000/")

    def test_loads_correctly(self):
        time.sleep(5)
        self.assertTrue("Registration" in self.driver.title)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()