from SauceDemoTestcases.POM_stage1.pages.LoginPage import LoginPage
from SauceDemoTestcases.POM_stage1.pages.InventoryPage import InventoryPage

def test_Logout_UI(driver):

    """
    Title : Verify that a user can log out successfully from the application

    Steps :
    1. Login to the application with valid credentials.
    2. Verify that the user is on the inventory page.
    3. Click on the burger menu button to open the sidebar menu.
    4. Click on the logout link in the sidebar menu.
    5. Verify that the user is redirected to the login page after logging out.

    Stories  :JiRATICKEt- xyz
    """
    # Test Case: Verify that a user can log out successfully from the application

    login_page = LoginPage(driver)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.login_button()

    inventory_page = InventoryPage(driver)

    assert 'inventory' in driver.current_url

    inventory_page.is_inventory_page_displayed()
    inventory_page.click_burger_menu_button()
    inventory_page.click_logout_sidebar_link()

   # Verification: Check if the user is redirected to the login page
    assert driver.current_url == "https://www.saucedemo.com/"
    print("Logout successful, user is on the login page.")
