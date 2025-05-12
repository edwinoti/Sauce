import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.error_message = (By.XPATH, '/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3')
        self.driver = driver
        self.username = (By.ID, "user-name")
        self.password = (By.ID, "password")
        self.login_btn = (By.ID, "login-button")

    def load(self):
        logging.info("Opening login page")
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username, password):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.username)).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.login_btn).click()
        logging.info("Submitted login form")

    def get_error_message(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.error_message)).text
