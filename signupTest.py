from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# Start chrome
driver = webdriver.Chrome()

# Open page
driver.get("https://automationexercise.com/")
driver.maximize_window()

# Setting implicit wait
driver.implicitly_wait(5)

# Clicking on the signup 
driver.find_element(By.CSS_SELECTOR, "a[href='/login']").click()

# Entering the username
signupName = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Name']")
signupName.click()
signupName.send_keys("testecomm")

# Adding the email
signupEmail = driver.find_element(By.CSS_SELECTOR, "input[data-qa='signup-email']")
signupEmail.click()
signupEmail.send_keys("ecomm@yopmail.com")

# Scrolling the page if element is not visible in the current viewport
driver.execute_script("window.scrollBy(0, 100);")

# Clicking on the signup BUTTON
signupButton = driver.find_elements(By.XPATH, "//button[@data-qa='signup-button']")[0]
signupButton.click()

time.sleep(3)

# driver.get_screenshot_as_file("beforeClickingSignup.png")

# Checking if landed on correct page or not, after click on signup button
if driver.current_url == "https://automationexercise.com/signup":
    print("Correct signup page")
else:
    print("still on Login page")

# Printing the current url address
print("Current web URL is ------> " + driver.current_url)

