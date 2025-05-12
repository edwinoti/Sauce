import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.item_title = (By.XPATH, "//a[@id='item_1_title_link']/div")
        self.back_btn = (By.ID, "back-to-products")

    def click_product(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.item_title)).click()
        logging.info("Opened product details page")

    def go_back(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.back_btn)).click()
        logging.info("Returned to product listing")
