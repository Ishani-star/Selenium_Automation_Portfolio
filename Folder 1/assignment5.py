from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/tables")

table = driver.find_element(By.ID, "table1")

headers = table.find_elements(By.XPATH, ".//thead/tr/th")

print("Table Headers:")
for header in headers:
    print(header.text)

rows = table.find_elements(By.XPATH, ".//tbody/tr")

search_name = "Smith"
found = False

for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")

    values = [cell.text for cell in cells]

    print(values)

    if values[0] == search_name:
        print("Last Name:", values[0])
        print("First Name:", values[1])
        print("Email:", values[2])
        print("Due:", values[3])
        print("Web Site:", values[4])
        print("Action:", values[5])

        found = True
        break

assert found

print("Assignment 5 passed")

input("Press Enter to close browser...")

driver.quit()