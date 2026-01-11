import allure
from selenium.webdriver.common.by import By
from ecommerceSeleniumPython.pages.base_page import BasePage

class LoginPage(BasePage):
  
#  ---------- SIGNUP LOCATORS ----------
    NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='Name']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[data-qa='signup-email']")
    SIGNUP_BUTTON = (By.XPATH, "//button[@data-qa='signup-button']")
    
# ---------- LOGIN LOCATORS ----------
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    
# ---------- LOGIN ACTIONS ----------
    @allure.step("Login with username: {username}")
    def login(self, username, password):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)
    
# ---------- SIGNUP ACTIONS ----------   
    @allure.step("Enter signup name: {name}")     
    def enter_name(self, name):
        self.type(self.NAME_INPUT, name)

    @allure.step("Enter signup email: {email}")
    def enter_email(self, email):
        self.type(self.EMAIL_INPUT, email)

    @allure.step("Click signup button")
    def click_signup_button(self):
        self.click(self.SIGNUP_BUTTON)
        