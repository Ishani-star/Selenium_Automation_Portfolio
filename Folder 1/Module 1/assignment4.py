from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()

alert = driver.switch_to.alert
print("Alert:", alert.text)
alert.accept()

result = driver.find_element(By.ID, "result")
assert result.text == "You successfully clicked an alert"
print("Alert accepted successfully")

driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()

alert = driver.switch_to.alert
print("Confirm:", alert.text)
alert.dismiss()

result = driver.find_element(By.ID, "result")
assert result.text == "You clicked: Cancel"
print("Confirm dismissed successfully")

driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()

alert = driver.switch_to.alert
print("Prompt:", alert.text)
alert.send_keys("Ishani")
alert.accept()

result = driver.find_element(By.ID, "result")
assert result.text == "You entered: Ishani"
print("Prompt handled successfully")

print("Assignment 4 passed")

input("Press Enter to close browser...")

driver.quit()