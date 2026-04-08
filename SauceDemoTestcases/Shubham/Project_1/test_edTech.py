import pytest
from selenium import webdriver
from time import sleep, time
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions as wait

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

#Test Case 1:
#Validate the URL https://www.guvi.in is valid or not
def test_verify_url(driver):
    target_url = "https://www.guvi.in/"
    driver.get(target_url)
    assert driver.current_url == target_url


# Test Case 2:
#Validate title of web page is correct
def test_verify_webpage(driver):
    target_url = "https://www.guvi.in/"
    driver.get(target_url)
    actual_title = "HCL GUVI | Learn to code in your native language"
    WebDriverWait(driver, 10).until(EC.title_is(actual_title))
    assert driver.title == actual_title


#Test Case 3
#Verify visibility and clickability of the login button
def test_functionality_login(driver):
    driver.get("https://www.guvi.in/")

    #Verify Visibility:
    login_button = driver.find_element(By.ID, "login-btn")
    assert login_button.is_displayed() and login_button.is_enabled()
    #Verify Clickability
    login_button.click()
    sleep(5)
    current_url = driver.current_url
    assert current_url == "https://www.guvi.in/sign-in/?sourceUri=http%3A%2F%2Fwww.guvi.in%2F"

#Test Case 4
#Verify visibility and clickability of the SignUp button
def test_functionality_signup(driver):
    driver.get("https://www.guvi.in/")

    #Verify Visibility:
    signup_button = driver.find_element(By.XPATH, "//button[text()='Sign up']")
    assert signup_button.is_displayed() and signup_button.is_enabled()
    signup_button.click()
    sleep(5)
    current_url = driver.current_url
    assert current_url == "https://www.guvi.in/register/?sourceUri=http%3A%2F%2Fwww.guvi.in%2F"

#Test Case 5
#Verify navigation to the Sign-In page via the Sign-Up button
def test_signup_navigation(driver):
    driver.get("https://www.guvi.in/")

    signup_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Sign up']")))
    signup_button.click()

    WebDriverWait(driver, 10).until(EC.url_contains("register"))
    actual_url = driver.current_url

    assert "guvi.in/register" in actual_url


# Test Case 6
# Verify login functionality with valid credentials
def test_submit_button_functionality(driver):
    driver.get("https://www.guvi.in/")
    wait = WebDriverWait(driver, 15)

    wait.until(EC.element_to_be_clickable((By.ID, "login-btn"))).click()
    wait.until(EC.visibility_of_element_located((By.ID, "email"))).send_keys("sb1249952@gmail.com")
    driver.find_element(By.ID, "password").send_keys("4AI12me101@")
    wait.until(EC.element_to_be_clickable((By.ID, "login-btn"))).click()

    profile_icon = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "gravatar-wrap")))
    profile_icon.click()

    my_profile = wait.until(EC.presence_of_element_located((By.XPATH, "//p[text()='My Profile']")))

    driver.execute_script("arguments[0].click();", my_profile)
    wait.until(EC.url_contains("sb124995293331"))
    assert "sb124995293331" in driver.current_url

#Test Case 7
#Verify login functionality with valid credentials

def test_invalid_login(driver):
    driver.get("https://www.guvi.in/")
    wait = WebDriverWait(driver, 10)

    wait.until(EC.element_to_be_clickable((By.ID, "login-btn"))).click()
    wait.until(EC.element_to_be_clickable((By.ID, "email"))).send_keys("invalid@gmail.com")
    driver.find_element(By.ID, "password").send_keys("98fd12me654@")
    wait.until(EC.element_to_be_clickable((By.ID, "login-btn"))).click()

    error_message = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "invalid-feedback")))
    assert error_message.is_displayed()
    assert error_message.text == "Incorrect Email or Password"

#Test Case 8
# Verify the menu items like "courses", "LIVE Classes", and "Practice" are displayed
def test_verify_menu_items(driver):
    driver.get("https://www.guvi.in/")
    wait = WebDriverWait(driver, 15)

    wait.until(EC.element_to_be_clickable((By.XPATH, "//p[text()='LIVE Classes']"))).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//p[text()='Courses']"))).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//p[text()='Practice']"))).click()

#Test Case 9
#Validate that the Dobby Guvi Assistant is present on the page
def test_guvi_assistant(driver):
    driver.get("https://www.guvi.in/")
    wait = WebDriverWait(driver, 30)

    launcher = wait.until(EC.element_to_be_clickable((By.ID, "zs_fl_chat")))
    launcher.click()
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "siq_chatwindow")))
    try:
        wait.until(lambda d: d.find_element(By.CLASS_NAME, "header-title").text.strip() != "")
        assistant_header = driver.find_element(By.CLASS_NAME, "header-title")
        header_text = assistant_header.text
        print(f"Assistant Name Found: {header_text}")
        assert len(header_text) > 0
        assert "Mini" in header_text
    finally:
        driver.switch_to.default_content()

#Test Case 10
#Verify Logout functionality

def test_logout(driver):
    driver.get("https://www.guvi.in/")
    wait = WebDriverWait(driver, 20)

    wait.until(EC.element_to_be_clickable((By.ID, "login-btn"))).click()
    wait.until(EC.element_to_be_clickable((By.ID, "email"))).send_keys("sb1249952@gmail.com")
    driver.find_element(By.ID, "password").send_keys("4AI12me101@")
    # Click on the login button
    wait.until(EC.element_to_be_clickable((By.ID, "login-btn"))).click()

    profile_icon = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "gravatar-wrap")))
    profile_icon.click()
    # Click on the logout button
    logout = wait.until(EC.presence_of_element_located((By.XPATH, "//p[text()='Sign Out']")))

    driver.execute_script("arguments[0].click();", logout)
    wait.until(EC.url_contains("guvi.in"))
    assert "guvi.in" in driver.current_url

