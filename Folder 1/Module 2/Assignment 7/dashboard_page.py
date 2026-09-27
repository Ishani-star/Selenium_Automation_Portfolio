from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DashboardPage(BasePage):
    inventory_container = (By.ID, "inventory_container")

    def is_displayed(self):
        return self.wait.until(lambda driver: "/inventory.html" in driver.current_url)

    def get_inventory_text(self):
        return self.get_text(self.inventory_container)