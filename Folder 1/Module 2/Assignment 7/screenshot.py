import os

def take_screenshot(driver, name):
    os.makedirs("screenshots", exist_ok=True)
    driver.save_screenshot(os.path.join("screenshots", name))