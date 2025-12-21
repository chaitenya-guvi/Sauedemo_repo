from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_checkout_error_when_fields_are_empty():
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

        # Step 3: Verify header displays "Swag Labs"
        header_text = driver.find_element(By.CLASS_NAME, "app_logo").text
        assert header_text == "Swag Labs"
        print("Header verified: Swag Labs")

        # Step 4: Add a product to the cart
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

        # Step 5: Click on shopping cart icon
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        # Step 6: Click on Checkout button
        driver.find_element(By.ID, "checkout").click()

        # Step 7: Leave First Name, Last Name, and Postal Code empty
        driver.find_element(By.ID, "first-name").clear()
        driver.find_element(By.ID, "last-name").clear()
        driver.find_element(By.ID, "postal-code").clear()

        # Step 8: Click Continue
        driver.find_element(By.ID, "continue").click()

        # Step 9: Verify error message
        error_message = driver.find_element(By.CLASS_NAME, "error-message-container").text
        assert "Error: First Name is required" in error_message
        print("Error message verified:", error_message)

    finally:
        # Close browser
        time.sleep(2)
        driver.quit()


# Call the function
test_checkout_error_when_fields_are_empty()
