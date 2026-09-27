from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 10)

driver.get("https://the-internet.herokuapp.com/checkboxes")

checkboxes = wait.until(
    EC.presence_of_all_elements_located(
        (By.XPATH, "//input[@type='checkbox']")
    )
)

if not checkboxes[0].is_selected():
    checkboxes[0].click()

print("Checkbox selected:", checkboxes[0].is_selected())

assert checkboxes[0].is_selected()

driver.get("https://demoqa.com/auto-complete")

input_box = wait.until(
    EC.element_to_be_clickable(
        (By.ID, "autoCompleteMultipleInput")
    )
)

input_box.send_keys("Red")

suggestions = wait.until(
    EC.presence_of_all_elements_located(
        (By.XPATH, "//div[contains(@class,'auto-complete__option')]")
    )
)

for suggestion in suggestions:
    print("Suggestion:", suggestion.text)

    if suggestion.text == "Red":
        suggestion.click()
        print("Red selected")
        break

print("Assignment 3 passed")

input("Press Enter to close browser...")

driver.quit()
