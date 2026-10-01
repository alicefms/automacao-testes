from selenium.webdriver.common.by import By

from tests.pages.base_page import BasePage


class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")

    def submit_shipping_information(
        self, first_name: str, last_name: str, postal_code: str
    ) -> str:
        self.fill(self.FIRST_NAME, first_name)
        self.fill(self.LAST_NAME, last_name)
        self.fill(self.POSTAL_CODE, postal_code)
        self.click(self.CONTINUE_BUTTON)
        return self.wait_for_url("checkout-step-two.html")

    def finish_purchase(self) -> str:
        self.click(self.FINISH_BUTTON)
        return self.wait_for_url("checkout-complete.html")