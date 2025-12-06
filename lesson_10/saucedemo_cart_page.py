from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Saucedemo_cart_page:
    def __init__(self, driver):
        self.driver = driver

    def fill_name(self, first_name: str) -> None:
        """
        Вводит имя в поле формы.

        :param first_name: Имя пользователя.
        """
        # Ожидаем появления формы перед заполнением
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "first-name"))
        )
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)

    def fill_lastname(self, last_name: str) -> None:
        """
        Вводит фамилию в поле формы.

        :param last_name: Фамилия пользователя.
        """
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)

    def fill_postalcode(self, postal_code: str) -> None:
        """
        Вводит почтовый индекс в поле формы.

        :param postal_code: Почтовый индекс.
        """
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)

    def accept(self) -> None:
        """
        Нажимает кнопку Continue и ожидает загрузки итоговой страницы.
        """
        self.driver.find_element(By.ID, "continue").click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "summary_total_label")
            )
        )
