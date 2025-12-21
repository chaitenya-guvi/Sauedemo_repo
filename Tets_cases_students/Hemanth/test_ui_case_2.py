from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

def test_product_sorting_low_to_high():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    sort_dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    sort_dropdown.select_by_visible_text("Price (low to high)")
    time.sleep(2)

    # Get all prices from inventory page
    price_elements = driver.find_elements(By.CLASS_NAME, "inventory_item_price")

    prices = []
    for price in price_elements:
        prices.append(float(price.text.replace("$", "")))

    print("Prices after sorting:", prices)

    # Verify prices are sorted low to high
    assert prices == sorted(prices)

    driver.quit()