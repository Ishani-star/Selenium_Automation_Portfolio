from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given("I open the SauceDemo website")
def step_open_website(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://www.saucedemo.com/")

@when("I enter valid username and password")
def step_enter_credentials(context):
    context.driver.find_element(By.ID, "user-name").send_keys("standard_user")
    context.driver.find_element(By.ID, "password").send_keys("secret_sauce")

@when("I click the login button")
def step_click_login(context):
    context.driver.find_element(By.ID, "login-button").click()

@then("I should be logged in successfully")
def step_verify_login(context):
    assert "inventory.html" in context.driver.current_url
    print("Login successful")
    input("Press Enter to close browser...")
    context.driver.quit()