from driver_setup import get_driver
from pages.home_page import HomePage
from pages.login_page import LoginPage

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
