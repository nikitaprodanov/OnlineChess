from element import BasePageElement
from locators import MainPageLocators

class UsernameElement(BasePageElement):
    locator = 'username'

class PasswordElement(BasePageElement):
    locator = 'password'

class ConfirmElement(BasePageElement):
    locator = 'confirm_pswd'


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class RegisterPage(BasePage):
    username_field_element = UsernameElement()
    password_field_element = PasswordElement()
    confirm_pswd_element = ConfirmElement()

    def is_title_matches(self):
        return "Registration" in self.driver.title

    def click_register_button(self):
        element = self.driver.find_element(*MainPageLocators.REGISTER_BUTTON)
        element.click()


class LoginPage(BasePage):

    def is_login_found(self):
        return "Login" in self.driver.title

