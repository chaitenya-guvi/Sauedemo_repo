from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        """
        Constructor to initialize the WebDriver instance.

        :param driver: Selenium WebDriver object
        """
        self.driver = driver

    # ------------------- Locators -------------------

    username_input = (By.ID, "user-name")
    password_input = (By.ID, "password")
    login_button = (By.ID, "login-button")

    # ------------------- Actions -------------------

    def enter_username(self, username: str) -> None :
        """
        Enters the username into the username input field.

        :param username: Username to be entered
        """
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        """
        Enters the password into the password input field.

        :param password: Password to be entered
        """
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login_button(self):
        """
        Clicks Login button
        """
        self.driver.find_element(*self.login_button).click()

