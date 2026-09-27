from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

links = driver.find_elements(By.TAG_NAME, "a")

print("Total links:", len(links))

for link in links:
    print(link.text)

input("Press Enter to close browser...")
driver.quit()