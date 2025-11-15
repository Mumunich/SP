from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Saucedemo_authorization_page:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url: str):
        self.driver.get(url)

    def login(self, username: str):
        self.driver.find_element(By.ID, "user-name").send_keys(username)

    def password(self, pwd: str):
        self.driver.find_element(By.ID, "password").send_keys(pwd)

    def enter(self):
        self.driver.find_element(By.ID, "login-button").click()
        # Ожидание загрузки страницы товаров после входа
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
        )
