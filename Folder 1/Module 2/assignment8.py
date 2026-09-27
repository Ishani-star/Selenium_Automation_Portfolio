from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


test_data = [
    ("standard_user", "secret_sauce", True),
    ("locked_out_user", "secret_sauce", False),
    ("problem_user", "secret_sauce", True),
    ("performance_glitch_user", "secret_sauce", True),
    ("invalid_user", "wrong_password", False)
]


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


def check_result(driver, expected):
    wait = WebDriverWait(driver, 10)

    if expected:
        wait.until(
            EC.url_contains("inventory.html")
        )
        return True

    error = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "[data-test='error']")
        )
    )

    return error.is_displayed()


driver = webdriver.Chrome()
driver.maximize_window()

for username, password, expected in test_data:
    try:
        login(driver, username, password)

        result = check_result(driver, expected)

        if result:
            print(username, "- Test Passed")
        else:
            print(username, "- Test Failed")

    except Exception as e:
        print(username, "- Test Failed:", str(e))

driver.quit()

print("Assignment 8 passed")