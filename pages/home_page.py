from selenium.webdriver.common.by import By
from ecommerceSeleniumPython.utils.base_page import BasePage

class HomePage(BasePage):

    SIGNUP_LOGIN_LINK = (By.CSS_SELECTOR, "a[href='/login']")

    def open(self):
        self.driver.get("https://automationexercise.com/")

    def click_signup_login(self):
        self.click(self.SIGNUP_LOGIN_LINK)
