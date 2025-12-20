from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_inventory_and_checkout_price():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    inventory_price = driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div"
    ).text
    print("Inventory price verified:", inventory_price)
    time.sleep(1)

    #Here we are adding the bcakpack to the cart
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    time.sleep(1)

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(1)

    checkout_price = driver.find_element(By.CLASS_NAME, "inventory_item_price").text

    assert checkout_price == "$29.99"
    print("Checkout price verified:", checkout_price)

    driver.quit()
