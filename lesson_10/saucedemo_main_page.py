from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Saucedemo_main_page:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self, item_id: str) -> None:
        """
        Добавляет товар в корзину по его ID.

        :param item_id: ID товара (например, 'sauce-labs-backpack').
        """
        self.driver.find_element(By.ID, f"add-to-cart-{item_id}").click()

    def open_cart(self) -> None:
        """
        Открывает корзину покупок и ожидает её загрузки.
        """
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        # Ожидание загрузки страницы корзины
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "checkout"))
        )
