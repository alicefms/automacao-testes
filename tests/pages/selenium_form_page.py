from selenium.webdriver.common.by import By

from tests.pages.base_page import BasePage


class SeleniumFormPage(BasePage):
    TEXT_INPUT = (By.ID, "my-text-id")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def open(self, url: str) -> str:
        self._driver.get(url)
        return self._driver.title

    def submit_text(self, text: str) -> str:
        self.fill(self.TEXT_INPUT, text)
        previous_url = self._driver.current_url
        self.click(self.SUBMIT_BUTTON)
        return self.wait_for_url_change(previous_url)