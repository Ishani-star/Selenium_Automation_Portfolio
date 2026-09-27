import json
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


with open("test_data/testdata.json", "r") as file:
    data = json.load(file)


def take_screenshot(driver, name):
    os.makedirs("screenshots", exist_ok=True)
    driver.save_screenshot(f"screenshots/{name}.png")


def handle_alert(driver):
    try:
        alert = WebDriverWait(driver, 3).until(
            EC.alert_is_present()
        )

        print("Alert found:", alert.text)

        alert.accept()

        print("Alert handled successfully")

    except:
        print("No alert appeared")


def clear_existing_cart(driver, wait):

    driver.get(data["url"] + "view_cart")

    wait.until(
        EC.url_contains("/view_cart")
    )

    time.sleep(1)

    while True:

        remove_buttons = driver.find_elements(
            By.CSS_SELECTOR,
            "a.cart_quantity_delete"
        )

        if not remove_buttons:
            break

        driver.execute_script(
            "arguments[0].click();",
            remove_buttons[0]
        )

        time.sleep(1)

    print("Existing cart cleared")

    driver.get(data["url"])

    wait.until(
        EC.url_contains("automationexercise.com")
    )


def test_ecommerce():

    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 15)

    driver.maximize_window()

    try:

        driver.get(data["url"])

        print("Website opened")

        take_screenshot(driver, "01_home")


        login_link = wait.until(
            EC.element_to_be_clickable(
                (By.LINK_TEXT, "Signup / Login")
            )
        )

        login_link.click()

        email_box = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//input[@data-qa='login-email']")
            )
        )

        email_box.send_keys(data["email"])

        driver.find_element(
            By.XPATH,
            "//input[@data-qa='login-password']"
        ).send_keys(data["password"])

        driver.find_element(
            By.XPATH,
            "//button[@data-qa='login-button']"
        ).click()

        wait.until(
            lambda d: "Logged in as" in d.page_source
        )

        print("Login successful")

        take_screenshot(driver, "02_login")

        clear_existing_cart(driver, wait)


        products_link = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "a[href='/products']")
            )
        )

        driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            products_link
        )

        driver.execute_script(
            "arguments[0].click();",
            products_link
        )

        wait.until(
            EC.url_contains("/products")
        )

        search_box = wait.until(
            EC.visibility_of_element_located(
                (By.ID, "search_product")
            )
        )

        print("Products page opened")

        search_box.send_keys(data["product"])

        search_button = wait.until(
            EC.presence_of_element_located(
                (By.ID, "submit_search")
            )
        )

        driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            search_button
        )

        driver.execute_script(
            "arguments[0].click();",
            search_button
        )

        time.sleep(2)

        print("Product search successful")

        take_screenshot(driver, "03_product_search")


        product = data["product"]

        product_box = wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    f"//div[contains(@class,'product-image-wrapper')][.//p[normalize-space()='{product}']]"
                )
            )
        )

        assert product_box.is_displayed()

        print("Searched product verified")


        view_product = wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    f"//div[contains(@class,'product-image-wrapper')][.//p[normalize-space()='{product}']]//a[contains(.,'View Product')]"
                )
            )
        )

        driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            view_product
        )

        driver.execute_script(
            "arguments[0].click();",
            view_product
        )

        wait.until(
            EC.url_contains("/product_details/")
        )

        print("Product details opened")

        take_screenshot(driver, "04_product_details")


        quantity_box = wait.until(
            EC.visibility_of_element_located(
                (By.ID, "quantity")
            )
        )

        quantity_box.clear()

        quantity_box.send_keys(
            data["quantity"]
        )

        print(
            "Quantity set to:",
            data["quantity"]
        )

        take_screenshot(driver, "05_quantity_updated")


        add_to_cart = wait.until(
            EC.presence_of_element_located(
                (
                    By.CSS_SELECTOR,
                    "button.btn.btn-default.cart"
                )
            )
        )

        driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            add_to_cart
        )

        driver.execute_script(
            "arguments[0].click();",
            add_to_cart
        )

        time.sleep(2)

        print("Product added to cart")

        take_screenshot(driver, "06_product_added")

        handle_alert(driver)


        view_cart = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//u[contains(text(),'View Cart')]")
            )
        )

        view_cart.click()

        wait.until(
            EC.url_contains("/view_cart")
        )

        print("Cart opened")

        take_screenshot(driver, "07_cart")


        cart_product = wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//td[@class='cart_description']//a"
                )
            )
        ).text

        print(
            "Product in cart:",
            cart_product
        )

        assert cart_product == data["product"]


        cart_quantity = wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//td[@class='cart_quantity']//button"
                )
            )
        ).text

        print(
            "Quantity in cart:",
            cart_quantity
        )

        assert cart_quantity == data["quantity"]


        price_text = wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//td[@class='cart_price']//p"
                )
            )
        ).text

        print(
            "Product price:",
            price_text
        )


        total_text = wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//td[contains(@class,'cart_total')]"

                )
            )
        ).text

        print(
            "Total price:",
            total_text
        )


        price = int(
            price_text.replace("Rs.", "").strip()
        )

        quantity = int(
            cart_quantity
        )

        total = int(
            total_text.replace("Rs.", "").strip()
        )

        expected_total = price * quantity

        print(
            "Expected total:",
            expected_total
        )

        assert total == expected_total

        print("Cart verification successful")

        take_screenshot(driver, "08_cart_verified")

        handle_alert(driver)

        print("Assignment 1 completed successfully")


    finally:

        driver.quit()