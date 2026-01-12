from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import webdriver_manager.chrome
from time import sleep
import pytest


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
sleep(5)

#Creating the file
file_name = "Webpage_task_11.txt"

#Selecting the full body of the page
full_page_text = driver.find_element(By.TAG_NAME, "body").text
page_title = driver.title
current_url = driver.current_url

with open(file_name, "w", encoding="utf-8") as file:
    file.write(f"Source URL: {current_url}\n")
    file.write(f"Page Title: {page_title}\n")
    file.write("-" * 500 + "\n\n")
    file.write(full_page_text)

print(driver.title)
print(driver.current_url)

# URL of Homepage
def test_Homepage_positive():
    print(url)
    assert url == url

def test_Homepage_negative():
    print(url)
    assert url == driver.browser

# The test function for title
""" Positive Test for Title"""
def test_title_of_web_application_positive():
    print(driver.title)
    assert driver.title == driver.title

""" Negative Test for Title"""
def test_title_of_web_application_negative():
    print(driver.title)
    assert driver.title == driver.current_url


#Current URL of Dashboard after Login with Credentials
""" Positive Test for Dashboard URL"""
def test_URL_of_Homepage_positive():
    print(driver.current_url)
    assert driver.current_url == driver.current_url

""" Negative Test for Dashboard URL"""
def test_URL_of_Homepage_negative():
    print(driver.current_url)
    assert driver.current_url == driver.title




