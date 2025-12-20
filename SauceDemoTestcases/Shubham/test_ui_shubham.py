from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import webdriver_manager.chrome
from time import sleep
import pytest

# def test_ui_shubham()

url="https://www.saucedemo.com/"
#Open Google chrome
driver = webdriver.Chrome()

#Maximize the window
driver.maximize_window()

driver.get(url)
sleep(2)

#Finding the Username and adding value
webelement_of_email_input = driver.find_element(By.XPATH,"//input[@data-test='username']")
webelement_of_email_input.send_keys("standard_user")

#Finding the Password space and adding Value
webelement_of_password_input = driver.find_element(By.XPATH,"//input[@data-test='password']")
webelement_of_password_input.send_keys("secret_sauce")

# clicking on the Login Button
login_btn = driver.find_element(By.ID, "login-button")
login_btn.click()
sleep(2)

# #Clicking on the Twitter Icon
webelement_of_twitter = driver.find_element(By.ID, "social-twitter")
# webelement_of_twitter.click()

#Clicking on the menu button
webelement_of_menu = driver.find_element(By.ID, "react-burger-menu-btn")
webelement_of_menu.click()
sleep(2)

#Click o the About link
webelement_of_about = driver.find_element(By.ID, "about_sidebar_link")
webelement_of_about.click()