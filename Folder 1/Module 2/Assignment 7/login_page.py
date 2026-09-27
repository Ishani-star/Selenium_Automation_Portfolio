from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.config import BASE_URL

class LoginPage(BasePage):
    username = (By.ID, "user-name")
    password = (By.NAME, "password")
    login_button = (By.XPATH, "//input[@id='login-button']")

    def open(self):
        self.driver.get(BASE_URL)

    def login(self, username_value, password_value):
        self.enter_text(self.username, username_value)
        self.enter_text(self.password, password_value)
        self.click(self.login_button)