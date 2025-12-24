from ecommerceSeleniumPython.driver_setup import get_driver
from ecommerceSeleniumPython.pages.home_page import HomePage
from ecommerceSeleniumPython.pages.login_page import LoginPage

def test_signup():
    driver = get_driver()

    home = HomePage(driver)
    login = LoginPage(driver)

    home.open()
    home.click_signup_login()

    login.enter_name("testecomm")
    login.enter_email("ecomm@yopmail.com")
    login.click_signup_button()

    assert driver.current_url == "https://automationexercise.com/signup", \
        "Signup page not loaded"

    print("Signup test passed")

    driver.quit()
