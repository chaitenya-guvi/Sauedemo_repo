

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Launch browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# Open application
driver.get("https://www.saucedemo.com/")

# Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(2)

# Click menu icon
driver.find_element(By.ID, "react-burger-menu-btn").click()
time.sleep(2)

# Click logout
driver.find_element(By.ID, "logout_sidebar_link").click()
time.sleep(2)

# Verify logout (login button should be visible)
assert driver.find_element(By.ID, "login-button").is_displayed()
print("Logout is working as expected")

# Close browser
driver.quit()