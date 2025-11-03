from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shopping_cart_total():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    wait = WebDriverWait(driver, 10)
    wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
        )

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    wait.until(EC.presence_of_element_located((By.ID, "checkout")))

    driver.find_element(By.ID, "checkout").click()

    wait.until(EC.presence_of_element_located((By.ID, "first-name")))

    driver.find_element(By.ID, "first-name").send_keys("Ростислав")
    driver.find_element(By.ID, "last-name").send_keys("Коровяков")
    driver.find_element(By.ID, "postal-code").send_keys("630073")
    driver.find_element(By.ID, "continue").click()

    wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
    )

    total_element = driver.find_element(By.CLASS_NAME, "summary_total_label")
    total_text = total_element.text
    total_value = total_text.replace("Total: ", "")
    driver.quit()
    assert (
        total_value == "$58.29"
    ), f"Ожидался результат '$58.29', но получен '{total_value}'"
