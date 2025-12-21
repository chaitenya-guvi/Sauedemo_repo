from selenium import webdriver
import time

from SauceDemoTestcases.Yash.pages.login_page import LoginPage
from SauceDemoTestcases.Yash.pages.inventory_page import InventoryPage
from SauceDemoTestcases.Yash.pages.cart_page import CartPage


def test_remove_product_from_cart():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        driver.get("https://www.saucedemo.com/")

        # Login
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        # Verify inventory page
        assert "inventory" in driver.current_url
        print("Inventory page loaded")

        # Inventory actions
        inventory_page = InventoryPage(driver)
        inventory_page.add_bike_light_to_cart()

        assert inventory_page.get_cart_badge_count() == "1"
        print("Cart badge count is 1")

        inventory_page.open_cart()

        # Cart actions
        cart_page = CartPage(driver)
        assert cart_page.get_product_name() == "Sauce Labs Bike Light"
        print("Product visible in cart")

        cart_page.remove_product()
        time.sleep(1)

        assert cart_page.get_cart_items_count() == 0
        print("Product removed successfully")

    finally:
        time.sleep(2)
        driver.quit()


test_remove_product_from_cart()
