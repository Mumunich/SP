from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Saucedemo_authorization_page:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url: str) -> None:
        """
        Открывает указанный URL в браузере.

        :param url: Адрес страницы для открытия.
        """
        self.driver.get(url)

    def login(self, username: str) -> None:
        """
        Вводит имя пользователя в поле ввода.

        :param username: Имя пользователя.
        """
        self.driver.find_element(By.ID, "user-name").send_keys(username)

    def password(self, pwd: str) -> None:
        """
        Вводит пароль в поле ввода.

        :param pwd: Пароль пользователя.
        """
        self.driver.find_element(By.ID, "password").send_keys(pwd)

    def enter(self) -> None:
        """
        Нажимает кнопку входа и ожидает загрузки страницы товаров.
        """
        self.driver.find_element(By.ID, "login-button").click()
        # Ожидание загрузки страницы товаров после входа
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
        )
