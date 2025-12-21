import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    # Initialize Firefox browser
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()

def login(driver):
    """Reusable login function"""
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(1)  # wait for page to load

def test_price_sorted_low_to_high(driver):
    login(driver)

    # Select sorting: Price low to high
    dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
    dropdown.click()
    dropdown.find_element(By.XPATH, "//option[text()='Price (low to high)']").click()
    time.sleep(1)  # wait for sorting

    # Get all product prices
    prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    previous_price = 0.0

    # Validate ascending order
    for price in prices:
        current_price = float(price.text.replace("$", ""))
        assert current_price >= previous_price, \
            f"Products not sorted Low to High. Error at price: {current_price}"
        previous_price = current_price

    print("Products are sorted Low to High successfully.")

def test_logout(driver):
    login(driver)

    # Open menu
    menu_button = driver.find_element(By.ID, "react-burger-menu-btn")
    menu_button.click()
    time.sleep(1)  # wait for menu animation

    # Click logout
    logout_link = driver.find_element(By.ID, "logout_sidebar_link")
    logout_link.click()
    time.sleep(1)  # wait for redirect

    # Verify login button is visible
    login_button = driver.find_element(By.ID, "login-button")
    assert login_button.is_displayed(), "Logout failed: Login button not visible"
    print("Logout successful.")
