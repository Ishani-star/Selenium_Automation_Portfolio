from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")
driver.maximize_window()

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.NAME, "password").send_keys("secret_sauce")

driver.find_element(By.XPATH, "//input[@id='login-button']").click()

assert "/inventory.html" in driver.current_url

print("Login successful")
print("Current URL:", driver.current_url)

input("Press Enter to close browser...")

driver.quit()