import pytest
from ecommerceSeleniumPython.utils.driver_factory import get_driver


@pytest.fixture
def driver():
    driver = get_driver(headless=True)
    yield driver
    driver.quit()
