import pytest
from guara.application import Application
from selenium.webdriver.remote.webdriver import WebDriver

from tests.fixtures.driver import driver


@pytest.fixture
def app(driver: WebDriver) -> Application:
    return Application(driver)