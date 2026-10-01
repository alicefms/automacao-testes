from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


Locator = tuple[str, str]


class BasePage:
    def __init__(self, driver: WebDriver, timeout: float = 10) -> None:
        self._driver = driver
        self._timeout = timeout

    def wait_visible(self, locator: Locator) -> WebElement:
        return WebDriverWait(self._driver, self._timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def click(self, locator: Locator) -> None:
        self.wait_visible(locator).click()

    def fill(self, locator: Locator, value: str) -> None:
        element = self.wait_visible(locator)
        element.clear()
        element.send_keys(value)

    def wait_for_url(self, fragment: str) -> str:
        WebDriverWait(self._driver, self._timeout).until(EC.url_contains(fragment))
        return self._driver.current_url

    def wait_for_url_change(self, previous_url: str) -> str:
        WebDriverWait(self._driver, self._timeout).until(
            EC.url_changes(previous_url)
        )
        return self._driver.current_url