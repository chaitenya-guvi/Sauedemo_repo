from selenium.webdriver.common.by import By

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
