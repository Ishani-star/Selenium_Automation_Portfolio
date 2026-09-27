from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 10)

driver.get("https://the-internet.herokuapp.com/windows")

original_window = driver.current_window_handle

driver.find_element(By.LINK_TEXT, "Click Here").click()

wait.until(lambda d: len(d.window_handles) == 2)

for window in driver.window_handles:
    if window != original_window:
        driver.switch_to.window(window)
        break

new_window_text = wait.until(
    EC.visibility_of_element_located(
        (By.TAG_NAME, "h3")
    )
)

print("New Window:", new_window_text.text)

assert new_window_text.text == "New Window"

driver.close()

driver.switch_to.window(original_window)

print("Original Window:", driver.title)

driver.get("https://the-internet.herokuapp.com/iframe")

wait.until(
    EC.frame_to_be_available_and_switch_to_it(
        (By.ID, "mce_0_ifr")
    )
)

editor = wait.until(
    EC.presence_of_element_located(
        (By.ID, "tinymce")
    )
)

driver.execute_script(
    "arguments[0].innerHTML = 'Selenium Iframe Test';",
    editor
)

text = editor.text

print("Iframe Text:", text)

assert text == "Selenium Iframe Test"

driver.switch_to.default_content()

heading = wait.until(
    EC.visibility_of_element_located(
        (By.TAG_NAME, "h3")
    )
)

print("Iframe Page:", heading.text)

assert heading.text == "An iFrame containing the TinyMCE WYSIWYG Editor"

print("Assignment 6 passed")

input("Press Enter to close browser...")

driver.quit()