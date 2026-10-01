import tempfile
from collections.abc import Iterator

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.fixture
def driver() -> Iterator[WebDriver]:
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False,
        },
    )

    with tempfile.TemporaryDirectory() as user_data_dir:
        chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
        browser = webdriver.Chrome(options=chrome_options)
        try:
            yield browser
        finally:
            browser.quit()