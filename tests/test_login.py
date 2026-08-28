from selenium.webdriver.common.by import By 
from selenium import webdriver
from tests.fixtures.driver import driver

URL = "https://www.saucedemo.com/"

def test_login_com_sucesso(driver):

    driver.get(URL)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    assert "inventory" in driver.current_url
def test_login_credenciais_invalidas(driver):
    driver.get(URL)
    driver.find_element(By.ID, "user-name").send_keys("usuario_invalido")
    driver.find_element(By.ID, "password").send_keys("senha_invalida")
    driver.find_element(By.ID, "login-button").click()

    erro = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
    assert "Username and password do not match" in erro
def test_usuario_bloqueado(driver):
    driver.get(URL)
    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    erro = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
    print(erro)
    assert "Sorry, this user has been locked out" in erro