from selenium.webdriver.common.by import By

from tests.pages.base_page import BasePage


class CartPage(BasePage):
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def start_checkout(self) -> str:
        self.click(self.CHECKOUT_BUTTON)
        return self.wait_for_url("checkout-step-one.html")