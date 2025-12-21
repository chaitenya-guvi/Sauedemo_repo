from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch Chrome
driver = webdriver.Chrome()

# Open Google home page
driver.get("https://www.saucedemo.com/")

time.sleep(5)

webelement_of_email_input = driver.find_element(By.NAME,"user-name")
webelement_of_email_input.send_keys("standard_user")
time.sleep(2)

webelement_of_password_input = driver.find_element(By.NAME,"password")
webelement_of_password_input.send_keys("secret_sauce")
time.sleep(2)
webelement_of_login_button = driver.find_element(By.ID,"login-button")
webelement_of_login_button.click()
time.sleep(5)
webelement_of_ham_burger_icon = driver.find_element(By.ID,"react-burger-menu-btn")
webelement_of_ham_burger_icon.click()
time.sleep(5)

#logout
webelement_of_logout_button = driver.find_element(By.ID,"logout_sidebar_link")
webelement_of_logout_button.click()
time.sleep(5)
driver.quit()
