from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self,driver):
        """
        Constructor to initialize the WebDriver instance.

        """
        self.driver = driver

    # ------------------- Locators -------------------
    inventory_page = (By.CLASS_NAME, "inventory_list")
    sort_dropdown = (By.CLASS_NAME, "product_sort_container")
    price = (By.CLASS_NAME, "inventory_item_price")
    

    # ------------------- Actions -------------------
    def is_inventory_page_displayed(self) -> bool:
        """
        Checks if the inventory page is displayed.

        :return: True if inventory page is displayed, False otherwise
        """
        return self.driver.find_element(*self.inventory_page).is_displayed()

    def click_sort_dropdown(self) -> None:
        """
        Clicks on the sort dropdown
        """
        self.driver.find_element(*self.sort_dropdown).click()

    def get_price_values(self):
        """
        Fetches price values from the inventory items.

        :return: List of price values as floats
        """
        prices = self.driver.find_elements(*self.price)
        return [float(p.text.replace("$", "")) for p in prices]
    
