import allure
from selenium.webdriver.common.by import By
from ecommerceSeleniumPython.pages.base_page import BasePage

class HomePage(BasePage):

    SIGNUP_LOGIN_LINK = (By.CSS_SELECTOR, "a[href='/login']")
    PRODUCTS_TITLE = (By.CLASS_NAME, "title")
    
    def open(self):
        self.driver.get("https://automationexercise.com/")
    
    @allure.step("Click Signup / Login link")    
    def click_signup_login(self):
        self.click(self.SIGNUP_LOGIN_LINK)

    @allure.step("Verify products page is displayed")
    def is_products_page_displayed(self):
        return self.driver.find_element(*self.PRODUCTS_TITLE).is_displayed()
