#from utils.driver_factory import get_driver
from ecommerceSeleniumPython.pages.login_page import LoginPage
from ecommerceSeleniumPython.pages.home_page import HomePage
from ecommerceSeleniumPython.config.config import BASE_URL, USERNAME, PASSWORD

def test_login(driver):
    #driver = get_driver()
    driver.get(BASE_URL)

    login_page = LoginPage(driver)
    home_page = HomePage(driver)

    login_page.login(USERNAME, PASSWORD)

    assert home_page.is_products_page_displayed()
    print("Login Test Passed")

    driver.quit()
