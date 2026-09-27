from behave import given, when, then
from selenium import webdriver
from pages.login_page import LoginPage

@given("I open the SauceDemo website")
def step_open_website(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://www.saucedemo.com/")
    context.login_page = LoginPage(context.driver)

@when('I enter username "{username}" and password "{password}"')
def step_enter_credentials(context, username, password):
    context.login_page.enter_username(username)
    context.login_page.enter_password(password)

@when("I click the login button")
def step_click_login(context):
    context.login_page.click_login()

@then('the login result should be "{result}"')
def step_verify_login(context, result):
    if result == "success":
        assert "inventory.html" in context.driver.current_url
        print("Login successful")
    elif result == "locked":
        message = context.driver.find_element("css selector", "[data-test='error']").text
        assert "locked out" in message
        print("Locked user verified")
    elif result == "invalid":
        message = context.driver.find_element("css selector", "[data-test='error']").text
        assert "Username and password do not match" in message
        print("Invalid user verified")
    input("Press Enter to close browser...")
    context.driver.quit()