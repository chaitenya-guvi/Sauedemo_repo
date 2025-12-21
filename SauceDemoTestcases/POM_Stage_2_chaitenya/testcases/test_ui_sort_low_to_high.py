from SauceDemoTestcases.POM_Stage_2_chaitenya.pages.LoginPage import LoginPage
from SauceDemoTestcases.POM_Stage_2_chaitenya.pages.InventoryPage import InventoryPage

def test_ui_low_to_high(driver):

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)


    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login_button()

    assert 'inventory' in driver.current_url

    inventory_page.select_sort_option("Price (low to high)")
    prices = inventory_page.get_all_prices()
    prices = inventory_page.remove_dolar_from_prices(prices)

    assert  prices == sorted(prices)

def test_ui_high_to_low(driver):

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)


    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login_button()

    assert 'inventory' in driver.current_url

    inventory_page.select_sort_option("Price (high to low)")
    prices = inventory_page.get_all_prices()
    prices = inventory_page.remove_dolar_from_prices(prices)

    # verify if prices are sorted high to low
    assert  prices == sorted(prices, reverse=True)



