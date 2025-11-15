import pytest
from selenium import webdriver
from calculator_page import Calculator


def test_calculator_addition():
    # Создание и настройка драйвера
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)

    # Создание объекта страницы
    calculator_page = Calculator(driver)

    # Действия
    calculator_page.open("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    calculator_page.set_delay("45")
    calculator_page.click_button("7")
    calculator_page.click_button("+")
    calculator_page.click_button("8")
    calculator_page.click_button("=")

    # Получаем результат
    result = calculator_page.get_result_text()

    # Проверка
    assert result == "15", f"Ожидался результат 15, но получен {result}"

    # Закрытие драйвера
    driver.quit()
    