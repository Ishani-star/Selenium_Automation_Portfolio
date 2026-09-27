import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    time.sleep(5)
    driver.quit()


def login(driver, username, password):
    driver.get("https://www.saucedemo.com/")

    wait = WebDriverWait(driver, 10)

    wait.until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    ).send_keys(username)

    wait.until(
        EC.visibility_of_element_located((By.ID, "password"))
    ).send_keys(password)

    wait.until(
        EC.element_to_be_clickable((By.ID, "login-button"))
    ).click()


def test_valid_login(driver):
    login(driver, "standard_user", "secret_sauce")

    WebDriverWait(driver, 10).until(
        EC.url_contains("inventory.html")
    )

    assert "inventory.html" in driver.current_url


def test_locked_user(driver):
    login(driver, "locked_out_user", "secret_sauce")

    error = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "[data-test='error']")
        )
    )

    assert "locked out" in error.text.lower()


def test_invalid_login(driver):
    login(driver, "invalid_user", "wrong_password")

    error = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "[data-test='error']")
        )
    )

    assert error.is_displayed()


if __name__ == "__main__":
    pytest.main([
        "-v",
        "assignment9.py",
        "--html=report.html",
        "--self-contained-html"
    ])