from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from tests.fixtures.driver import driver

def test_navegacao(driver):
    # Inicializa o ChromeDriver automaticamente

    try:
        driver.get("https://www.selenium.dev/selenium/web/web-form.html")
        time.sleep(2)  # Pausa apenas para você visualizar a ação

        driver.find_element(By.ID, "my-text-id").send_keys("foo")
        driver.find_element(By.XPATH, "/html/body/main/div/form/div/div[2]/button").click()
                
        time.sleep(3)  # Pausa apenas para você visualizar a ação
       

    finally:
        # Fecha o navegador e encerra o processo
        driver.quit()
