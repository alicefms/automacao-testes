from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from tests.pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def open(self, url: str) -> str:
        self._driver.get(url)
        return self._driver.title

    def login(self, username: str, password: str) -> str:
        self.fill(self.USERNAME, username)
        self.fill(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)
        WebDriverWait(self._driver, self._timeout).until(
            EC.any_of(
                EC.url_contains("inventory.html"),
                EC.visibility_of_element_located(self.ERROR_MESSAGE),
            )
        )
        if "inventory.html" in self._driver.current_url:
            return self._driver.current_url
        return self.wait_visible(self.ERROR_MESSAGE).text