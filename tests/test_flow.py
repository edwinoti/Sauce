from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_invalid_login_shows_error(browser):
    login = LoginPage(browser)

    login.load()
    login.login("standard_userXX", "wrong_pass")

    error_msg = login.get_error_message()

    assert "Epic sadface: Username and password do not match any user in this service" in error_msg

def test_flow(browser):
    login = LoginPage(browser)
    inventory = InventoryPage(browser)
    cart = CartPage(browser)

    login.load()
    login.login("standard_user", "secret_sauce")

    # Validate successful login
    WebDriverWait(browser, 10).until(EC.url_contains("inventory"))
    assert "inventory" in browser.current_url

    inventory.add_to_cart()
    inventory.go_to_cart()

    assert "cart" in browser.current_url

    cart.click_product()
    assert "inventory-item.html" in browser.current_url

    cart.go_back()
    assert "inventory" in browser.current_url


