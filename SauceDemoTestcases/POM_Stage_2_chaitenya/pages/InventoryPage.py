from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class InventoryPage:
    def __init__(self,driver):
        """
        Constructor to initialize the WebDriver instance.

        """
        self.driver = driver

    # ------------------- Locators -------------------
    inventory_container = (By.ID, "inventory_container")
    burger_menu_button = (By.ID, "react-burger-menu-btn")
    logout_siedebar_link = (By.ID, "logout_sidebar_link")
    select_dropdown = (By.CLASS_NAME, "product_sort_container")
    all_prices_locator = (By.CLASS_NAME, "inventory_item_price")


    # ------------------- Actions -------------------
    def is_inventory_page_displayed(self) -> bool:
        """
        Checks if the inventory page is displayed.

        :return: True if inventory page is displayed, False otherwise
        """
        return self.driver.find_element(*self.inventory_container).is_displayed()

    def click_burger_menu_button(self) -> None:
        """
        Clicks the hamburger icon on the left
        """

        self.driver.find_element(*self.burger_menu_button).click()

    def click_logout_sidebar_link(self) -> None:
        """
        Clicks the logout link in the sidebar menu
        """
        self.driver.find_element(*self.logout_siedebar_link).click()

    def select_sort_option(self, option_text: str) -> None:
        """
        Selects a sorting option from the dropdown.

        :param option_value: The value attribute of the option to select
        """
        dropdown = Select(self.driver.find_element(*self.select_dropdown))
        dropdown.select_by_visible_text(option_text)

    def get_all_prices(self) -> list:
        """
        Retrieves all item prices from the inventory page.

        :return: List of item prices as floats
        """
        price_elements = self.driver.find_elements(*self.all_prices_locator)
        price_list = []
        for ele in price_elements:
           price_list.append(ele.text)

        return price_list

    def remove_dolar_from_prices(self,list_of_prices : list) -> list:
        """
        Removes the dollar sign from a list of price strings and converts them to floats.

        expected list = ['$7.99', '$9.99', '$15.99', '$15.99', '$29.99', '$49.99']
        output list = ['7.99', '9.99', '15.99', '15.99', '29.99', '49.99']

        :param list_of_prices: List of price strings with dollar signs
        :return: List of prices as floats without dollar signs
        """
        output_list= []
        for price in list_of_prices:
            price_value = price.replace("$","")
            output_list.append(float(price_value))

        return output_list