from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pytest

def test_ui_about():
    url = "https://www.saucedemo.com/"
    #Open Google chrome
    driver = webdriver.Chrome()

    #Maximize the window
    driver.maximize_window()

    driver.get(url)
    sleep(2)

    #Finding the Username and adding value
    webelement_of_email_input = driver.find_element(By.XPATH, "//input[@data-test='username']")
    webelement_of_email_input.send_keys("standard_user")

    #Finding the Password space and adding Value
    webelement_of_password_input = driver.find_element(By.XPATH, "//input[@data-test='password']")
    webelement_of_password_input.send_keys("secret_sauce")

    # clicking on the Login Button
    login_btn = driver.find_element(By.ID, "login-button")
    login_btn.click()
    sleep(5)


    webelement_of_twitter = driver.find_element(By.CLASS_NAME, "social_twitter")
    webelement_of_twitter.click()
    sleep(2)

    # print("The current URL is : " + driver.current_url)

    def switch_to_elemental_selenium_window(self):                                     
        all_window_handles = self.driver.window_handles
        print("Line 26 ---- The list of all windows is : ")
        print(all_window_handles)

        for window_tab_code in all_window_handles:
            if (window_tab_code == self.driver.current_window_handle):
                print("this is the first iteration , I am on the main window handle and there is n need to switch")
            else:
                print("The current URL before switching is : " + self.driver.current_url)
                self.driver.switch_to.window(window_tab_code)
                sleep(5)
                print("The current url after switching is   : " + self.driver.current_url)
                print("The current title after switching is   : " + self.driver.title)


    assert driver.current_url == "https://x.com/saucelabs"
    print("Test Case 2 Passed")
    #close browser
    sleep(5)
    driver.quit()