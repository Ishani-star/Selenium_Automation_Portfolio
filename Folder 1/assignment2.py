from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

driver.find_element(By.XPATH, "//button[text()='Start']").click()

message = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//div[@id='finish']/h4")
    )
)

print("Message:", message.text)

assert message.text == "Hello World!"

print("Assignment 2 passed")

input("Press Enter to close browser...")

driver.quit()