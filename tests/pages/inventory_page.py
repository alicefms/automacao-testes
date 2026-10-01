from selenium.webdriver.common.by import By

from tests.pages.base_page import BasePage


class InventoryPage(BasePage):
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def add_product(self, product_id: str) -> None:
        self.click((By.ID, f"add-to-cart-{product_id}"))

    def open_cart(self) -> str:
        self.click(self.CART_LINK)
        return self.wait_for_url("cart.html")