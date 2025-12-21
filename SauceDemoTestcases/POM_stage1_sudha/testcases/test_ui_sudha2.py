from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)

# ---------- LOGIN ----------
driver.get("https://www.saucedemo.com/")

wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list")))

# ---------- TEST CASE 9 ----------
driver.find_element(By.ID, "react-burger-menu-btn").click()

wait.until(EC.visibility_of_element_located((By.ID, "inventory_sidebar_link")))

menu_items = {
    "All Items": "inventory_sidebar_link",
    "About": "about_sidebar_link",
    "Logout": "logout_sidebar_link",
    "Reset App State": "reset_sidebar_link"
}

for name, item_id in menu_items.items():
    element = driver.find_element(By.ID, item_id)
    assert element.is_displayed(), f"❌ {name} menu option is NOT visible"
    print(f"✅ {name} menu option is visible")

print("✅ Test Case 2 Passed: Side menu verified")

driver.quit()
