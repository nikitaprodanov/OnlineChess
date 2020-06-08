import unittest
from selenium import webdriver
import time
import page

class BasicOnlineChessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("./chromedriver")
        self.driver.get("http://127.0.0.1:5000/")

    def test_loads_correctly(self):
        time.sleep(5)
        self.assertTrue("Registration" in self.driver.title)

    def test_login_correct(self):
        register_page = page.RegisterPage(self.driver)
        assert register_page.is_title_matches()
        register_page.username_field_element = "User16"
        register_page.password_field_element = "test"
        register_page.confirm_pswd_element = "test"
        register_page.click_register_button()
        submit_results_page = page.LoginPage(self.driver)
        assert submit_results_page.is_login_found()


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()