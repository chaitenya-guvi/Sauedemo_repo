from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)

# ---------- LOGIN ----------
driver.get("https://www.saucedemo.com/")

wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list")))

# ---------- TEST CASE 8 ----------
sort_dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
sort_dropdown.select_by_value("lohi")

time.sleep(2)

prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
price_values = [float(p.text.replace("$", "")) for p in prices]

assert price_values == sorted(price_values), "❌ Prices are NOT sorted Low to High"
print("✅ Test Case 1 Passed: Prices sorted Low to High")

driver.quit()
