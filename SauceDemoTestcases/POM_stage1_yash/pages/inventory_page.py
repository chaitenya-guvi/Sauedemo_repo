from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    inventory_list = (By.CLASS_NAME, "inventory_list")
    sort_dropdown = (By.CLASS_NAME, "product_sort_container")
    prices = (By.CLASS_NAME, "inventory_item_price")

    def wait_for_inventory_page(self):
        self.wait.until(EC.visibility_of_element_located(self.inventory_list))

    def sort_price_low_to_high(self):
        dropdown = Select(self.driver.find_element(*self.sort_dropdown))
        dropdown.select_by_value("lohi")

    def get_all_prices(self):
        price_elements = self.driver.find_elements(*self.prices)
        return [float(p.text.replace("$", "")) for p in price_elements]
