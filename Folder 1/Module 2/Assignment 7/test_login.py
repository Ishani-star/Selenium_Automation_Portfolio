from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.csv_reader import read_csv

class TestLogin:
    def test_login(self, driver):
        data = read_csv("testdata/login_data.csv")[0]

        login_page = LoginPage(driver)
        dashboard_page = DashboardPage(driver)

        login_page.open()

        login_page.login(
            data["username"],
            data["password"]
        )

        assert dashboard_page.is_displayed()
        assert "/inventory.html" in dashboard_page.get_current_url()

        inventory_text = dashboard_page.get_inventory_text()

        assert inventory_text

        print("Login successful")
        print("Current URL:", dashboard_page.get_current_url())
        print("Dashboard loaded successfully")
        print("Assignment 7 passed")