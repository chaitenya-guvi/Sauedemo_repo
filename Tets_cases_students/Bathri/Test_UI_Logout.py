from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

def test_Logout_UI():
    # Test Case: Verify that a user can log out successfully from the application

    url = "https://www.saucedemo.com/"
    driver = webdriver.Chrome()

    driver.get(url)
    driver.maximize_window()
    sleep(2)
    webelement_of_username_input = driver.find_element(By.ID, "user-name")
    webelement_of_username_input.send_keys("standard_user")

    webelement_of_password_input = driver.find_element(By.ID, "password")
    webelement_of_password_input.send_keys("secret_sauce")
    sleep(2)
    webelement_of_login_button = driver.find_element(By.ID, "login-button")
    webelement_of_login_button.click()
    sleep(2)

    # Click on the menu button
    webelement_of_menu_button = driver.find_element(By.ID, "react-burger-menu-btn")
    webelement_of_menu_button.click()
    sleep(2)

    # Click on the logout link
    webelement_of_logout_link = driver.find_element(By.ID, "logout_sidebar_link")
    webelement_of_logout_link.click()
    sleep(2)
    # Verification: Check if the user is redirected to the login page
    assert driver.current_url == "https://www.saucedemo.com/"
    print("Logout successful, user is on the login page.")