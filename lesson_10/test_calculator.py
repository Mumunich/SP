import allure
from selenium import webdriver
from calculator_page import Calculator


@allure.feature("Calculator")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Проверка сложения в калькуляторе с задержкой")
@allure.description(
    """
    Тест проверяет работу калькулятора с установленной задержкой:
    1. Открыть страницу калькулятора.
    2. Установить задержку 45 секунд.
    3. Ввести выражение 7 + 8.
    4. Нажать '=' и дождаться результата.
    5. Проверить, что результат равен 15.
"""
)
def test_calculator_addition():
    @allure.step("Создание и настройка драйвера")
    def setup_driver():
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        return driver

    @allure.step("Открыть страницу калькулятора")
    def open_calculator_page(calculator_page):
        calculator_page.open(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )

    @allure.step("Установить задержку {delay} секунд")
    def set_calculator_delay(calculator_page, delay):
        calculator_page.set_delay(delay)

    @allure.step("Ввести выражение {num1} {operation} {num2}")
    def enter_calculation(calculator_page, num1, operation, num2):
        calculator_page.click_button(num1)
        calculator_page.click_button(operation)
        calculator_page.click_button(num2)

    @allure.step("Нажать кнопку '='")
    def press_equals(calculator_page):
        calculator_page.click_button("=")

    @allure.step("Получить результат вычисления")
    def get_calculation_result(calculator_page):
        return calculator_page.get_result_text()

    @allure.step("Проверить, что результат равен {expected}"
                 "(получено: {actual})")
    def verify_result(actual, expected):
        assert actual == expected, f"Ожидался результат {expected},"
        " но получен {actual}"

    @allure.step("Закрыть драйвер")
    def close_driver(driver):
        driver.quit()

    driver = setup_driver()
    calculator_page = Calculator(driver)

    open_calculator_page(calculator_page)
    set_calculator_delay(calculator_page, "45")
    enter_calculation(calculator_page, "7", "+", "8")
    press_equals(calculator_page)
    result = get_calculation_result(calculator_page)
    verify_result(result, "15")

    close_driver(driver)
