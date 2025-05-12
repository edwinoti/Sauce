import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_to_cart_btn = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        self.cart_icon = (By.XPATH, "//div[@id='shopping_cart_container']/a/span")

    def add_to_cart(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.add_to_cart_btn)).click()
        logging.info("Added product to cart")

    def go_to_cart(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.cart_icon)).click()
        logging.info("Navigated to cart")
