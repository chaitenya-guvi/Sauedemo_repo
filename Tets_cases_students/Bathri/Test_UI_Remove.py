# Verify user can remove a product from the shopping cart
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

def test_ui_remove_product():

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
    # Adding product to the cart
    webelement_of_addtocart_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    webelement_of_addtocart_button.click()
    sleep(2)
    # Navigate to the cart
    webelement_of_cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    webelement_of_cart_icon.click()
    sleep(2)
    # Remove the product from the cart
    webelement_of_remove_button = driver.find_element(By.ID, "remove-sauce-labs-backpack")
    webelement_of_remove_button.click()
    sleep(2)
    # Verification: Check if the cart is empty
    webelement_of_cart_badge = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
    assert len(webelement_of_cart_badge) == 0, "Cart is not empty after removing the product."
    print("Product successfully removed from the cart. Cart is empty.")
    driver.quit()


