import pytest
from selenium import webdriver
from saucedemo_authorization_page import Saucedemo_authorization_page
from saucedemo_main_page import Saucedemo_main_page
from saucedemo_checkout_page import Saucedemo_checkout_page
from saucedemo_cart_page import Saucedemo_cart_page
from selenium.webdriver.chrome.options import Options


def test_shopping_cart_total():
    # Создание и настройка драйвера
    chrome_options = Options()
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-password-manager-reauthentication")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False,
    "profile.default_content_setting_values.notifications": 2,
    "safebrowsing.enabled": False,
    "profile.password_manager_leak_detection": False
    })
    chrome_options.add_argument("--password-store=basic")

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(5)

    # Создание объектов страниц
    auth_page = Saucedemo_authorization_page(driver)
    main_page = Saucedemo_main_page(driver)
    cart_page = Saucedemo_cart_page(driver)  # на самом деле — checkout-step-one
    checkout_page = Saucedemo_checkout_page(driver)  # checkout-step-two

    # Действия
    auth_page.open("https://www.saucedemo.com/")
    auth_page.login("standard_user")
    auth_page.password("secret_sauce")
    auth_page.enter()

    main_page.add_to_cart("sauce-labs-backpack")
    main_page.add_to_cart("sauce-labs-bolt-t-shirt")
    main_page.add_to_cart("sauce-labs-onesie")
    main_page.open_cart()

    checkout_page.checkout()  # нажать Checkout на странице корзины

    cart_page.fill_name("Ростислав")
    cart_page.fill_lastname("Коровяков")
    cart_page.fill_postalcode("630073")
    cart_page.accept()
    # Получение результата
    total_value = checkout_page.get_result_text()
    # Закрытие драйвера
    driver.quit()
    # Проверка
    assert total_value == "$58.29", f"Ожидался '$58.29', получен '{total_value}'"
