from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_remove_product_from_cart():
    # Initialize WebDriver
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # Step 1: Open the application
        driver.get("https://www.saucedemo.com/")

        # Step 2: Login
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Step 3: Verify inventory page loads
        assert "inventory" in driver.current_url
        print("Inventory page loaded successfully")

        # Step 4: Add Sauce Labs Bike Light to cart
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()

        # Step 5: Verify cart badge count is 1
        cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        assert cart_badge == "1"
        print("Cart badge count is 1")

        # Step 6: Click shopping cart icon
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        # Step 7: Verify Sauce Labs Bike Light is visible in the cart
        product_name = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
        assert product_name == "Sauce Labs Bike Light"
        print("Sauce Labs Bike Light is visible in the cart")

        # Step 8: Click Remove button
        driver.find_element(By.ID, "remove-sauce-labs-bike-light").click()

        # Step 9: Verify item is no longer visible in the cart
        time.sleep(1)
        cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(cart_items) == 0
        print("Item removed successfully from the cart")

    finally:
        # Close browser
        time.sleep(2)
        driver.quit()


# Call the function
test_remove_product_from_cart()
