from selenium import webdriver
from SauceDemoTestcases.POM_stage1.pages.LoginPage import LoginPage
from SauceDemoTestcases.POM_stage1.pages.InventoryPage import InventoryPage

def test_price():
    # Test Case: Verify product sorting by Price (Low to High)

    url = "https://www.saucedemo.com/"
    driver = webdriver.Chrome()

    driver.get(url)
    driver.maximize_window()

    login_page = LoginPage(driver)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.login_button()

    inventory_page = InventoryPage(driver)
    inventory_page.sort_by_price_low_to_high()
    prices = inventory_page.get_all_product_prices()
    sorted_prices = sorted(prices)
    assert prices == sorted_prices, "Products are not sorted by Price (Low to High)"
    print("Products are sorted by Price (Low to High) successfully.")
    driver.quit()
    
