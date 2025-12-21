"""Test Case 1
Title: Verify user can remove a product from the shopping cart
Precondition:
User is able to login with valid credentials
User has at least one product added to the cart (Sauce Labs Bike Light)

Steps for test:
Verify inventory page loads after login
Add “Sauce Labs Bike Light” to the cart
Cart badge count should display 1
Click the shopping cart icon
Verify “Sauce Labs Bike Light” is visible in the cart
Click the Remove button next to “Sauce Labs Bike Light”

Verify the item is no longer visible in the cart

Expected:
Sauce Labs Bike Light should be removed successfully and should not appear in the cart
"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def test_remove_product_from_cart():
    # Chrome setup
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    wait = WebDriverWait(driver, 10)

    try:
        # Step 1: Open application
        driver.get("https://www.saucedemo.com/")

        # Step 2: Login with valid credentials
        wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Step 3: Verify inventory page loads
        wait.until(EC.url_contains("inventory"))
        assert "inventory" in driver.current_url

        # Step 4: Add Sauce Labs Bike Light to cart
        wait.until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bike-light"))
        ).click()

        # Step 5: Verify cart badge count = 1
        cart_badge = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
        )
        assert cart_badge.text == "1"

        # Step 6: Click shopping cart icon
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        # Step 7: Verify Sauce Labs Bike Light is visible in cart
        product_name = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name"))
        )
        assert product_name.text == "Sauce Labs Bike Light"

        # Step 8: Click Remove button
        wait.until(
            EC.element_to_be_clickable((By.ID, "remove-sauce-labs-bike-light"))
        ).click()

        # Step 9: Verify item is no longer visible in the cart
        removed_items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        assert len(removed_items) == 0

        print("✅ TEST PASSED: Product removed successfully from cart")

    finally:
        driver.quit()