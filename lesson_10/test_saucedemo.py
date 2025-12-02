import allure
import pytest
from selenium import webdriver
from saucedemo_authorization_page import Saucedemo_authorization_page
from saucedemo_main_page import Saucedemo_main_page
from saucedemo_checkout_page import Saucedemo_checkout_page
from saucedemo_cart_page import Saucedemo_cart_page
from selenium.webdriver.chrome.options import Options


@allure.feature("Saucedemo Shopping Cart")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Проверка итоговой суммы покупки в корзине")
@allure.description("""
    Тест проверяет правильность расчета итоговой суммы в корзине:
    1. Авторизоваться как standard_user.
    2. Добавить три товара в корзину.
    3. Перейти в корзину.
    4. Оформить заказ.
    5. Заполнить данные доставки.
    6. Проверить итоговую сумму ($58.29).
""")
def test_shopping_cart_total():
    @allure.step("Настройка драйвера Chrome с опциями")
    def setup_chrome_driver():
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
        return driver
    
    @allure.step("Создание объектов страниц")
    def create_page_objects(driver):
        auth_page = Saucedemo_authorization_page(driver)
        main_page = Saucedemo_main_page(driver)
        cart_page = Saucedemo_cart_page(driver)  # на самом деле — checkout-step-one
        checkout_page = Saucedemo_checkout_page(driver)  # checkout-step-two
        return auth_page, main_page, cart_page, checkout_page
    
    @allure.step("Авторизация пользователя {username}")
    def perform_authentication(auth_page, username, password):
        auth_page.open("https://www.saucedemo.com/")
        auth_page.login(username)
        auth_page.password(password)
        auth_page.enter()
    
    @allure.step("Добавление товаров в корзину: {items}")
    def add_items_to_cart(main_page, items):
        for item in items:
            main_page.add_to_cart(item)
    
    @allure.step("Открытие корзины покупок")
    def open_shopping_cart(main_page):
        main_page.open_cart()
    
    @allure.step("Переход к оформлению заказа")
    def proceed_to_checkout(checkout_page):
        checkout_page.checkout()
    
    @allure.step("Заполнение данных для доставки: {first_name} {last_name}, {postal_code}")
    def fill_shipping_info(cart_page, first_name, last_name, postal_code):
        cart_page.fill_name(first_name)
        cart_page.fill_lastname(last_name)
        cart_page.fill_postalcode(postal_code)
        cart_page.accept()
    
    @allure.step("Получение итоговой суммы")
    def get_total_amount(checkout_page):
        return checkout_page.get_result_text()
    
    @allure.step("Проверка итоговой суммы (ожидается {expected}, получено {actual})")
    def verify_total_amount(actual, expected):
        assert actual == expected, f"Ожидался '{expected}', получен '{actual}'"
    
    @allure.step("Закрытие браузера")
    def close_browser(driver):
        driver.quit()
    
    driver = setup_chrome_driver()
    auth_page, main_page, cart_page, checkout_page = create_page_objects(driver)
    
    perform_authentication(auth_page, "standard_user", "secret_sauce")
    add_items_to_cart(main_page, [
        "sauce-labs-backpack",
        "sauce-labs-bolt-t-shirt",
        "sauce-labs-onesie"
    ])
    open_shopping_cart(main_page)
    proceed_to_checkout(checkout_page)
    fill_shipping_info(cart_page, "Ростислав", "Коровяков", "630073")
    total_value = get_total_amount(checkout_page)
    verify_total_amount(total_value, "$58.29")
    
    close_browser(driver)
