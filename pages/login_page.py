from selenium.webdriver.common.by import By
from utils.base_page import BasePage

class LoginPage(BasePage):

    NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='Name']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[data-qa='signup-email']")
    SIGNUP_BUTTON = (By.XPATH, "//button[@data-qa='signup-button']")

    def enter_name(self, name):
        self.send_keys(self.NAME_INPUT, name)

    def enter_email(self, email):
        self.send_keys(self.EMAIL_INPUT, email)

    def click_signup_button(self):
        self.click(self.SIGNUP_BUTTON)
