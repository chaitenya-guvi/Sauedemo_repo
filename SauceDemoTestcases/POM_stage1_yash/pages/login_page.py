from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    username = (By.ID, "user-name")
    password = (By.ID, "password")
    login_button = (By.ID, "login-button")

    def login(self, username, password):
        self.wait.until(EC.visibility_of_element_located(self.username)).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.login_button).click()
