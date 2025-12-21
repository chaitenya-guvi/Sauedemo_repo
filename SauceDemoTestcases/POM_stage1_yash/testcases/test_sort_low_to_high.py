from selenium import webdriver
import time
from SauceDemoTestcases.POM_stage1_yash.pages.login_page import LoginPage
from SauceDemoTestcases.POM_stage1_yash.pages.inventory_page import InventoryPage

def test_sort_products_low_to_high():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        driver.get("https://www.saucedemo.com/")

        # Login
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        # Inventory page actions
        inventory_page = InventoryPage(driver)
        inventory_page.wait_for_inventory_page()
        inventory_page.sort_price_low_to_high()

        time.sleep(2)

        prices = inventory_page.get_all_prices()
        assert prices == sorted(prices), "❌ Prices are NOT sorted Low to High"
        print("✅ Test Case Passed: Prices sorted Low to High")

    finally:
        driver.quit()


test_sort_products_low_to_high()
