from selenium.webdriver.common.by import By

from tests.pages.base_page import BasePage


class ConfirmationPage(BasePage):
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def message(self) -> str:
        return self.wait_visible(self.COMPLETE_HEADER).text