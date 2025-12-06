from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Calculator:
    def __init__(self, driver):
        self.driver = driver

    def open(self, html: str) -> None:
        """
        Открывает указанный URL в браузере.

        :param html: URL страницы калькулятора.
        """
        self.driver.get(html)

    def set_delay(self, value: str) -> None:
        """
        Устанавливает значение задержки в поле ввода.

        :param value: Значение задержки в секундах.
        """
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(value)

    def click_button(self, text: str) -> None:
        """
        Нажимает кнопку калькулятора по её тексту.

        :param text: Текст на кнопке (например, '7', '+', '=', 'C').
        """
        # Кнопки имеют текст: '7', '+', '=', 'C' и т.д.
        button = self.driver.find_element(By.XPATH, f"//span[text()='{text}']")
        button.click()

    def get_result_text(self) -> str:
        """
        Ожидает появления результата и возвращает его текст.

        :return: Текст результата из поля "screen".
        """
        # Результат отображается в поле с классом screen
        WebDriverWait(self.driver, 50).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
        )
        # После ожидания возвращаем актуальный текст
        return self.driver.find_element(By.CLASS_NAME, "screen").text
