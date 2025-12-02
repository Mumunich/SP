from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Saucedemo_checkout_page:
    def __init__(self, driver):
        self.driver = driver

    def check_cart_list(self) -> None:
        """
        Ожидает загрузки списка товаров в корзине.
        """
        # Убедиться, что страница корзины загружена
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "cart_list"))
        )

    def checkout(self) -> None:
        """
        Нажимает кнопку Checkout и ожидает загрузки формы ввода данных.
        """
        self.driver.find_element(By.ID, "checkout").click()
        # После нажатия checkout попадаем на страницу формы — ждём её
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "first-name"))
        )

    def get_result_text(self) -> str:
        """
        Получает итоговую сумму из элемента на странице.

        :return: Строка с итоговой суммой (без префикса "Total: ").
        """
        total_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
        total_text = total_element.text
        return total_text.replace("Total: ", "")
