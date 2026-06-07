import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_visual_x11():
    # Configura o navegador Chromium
    options = webdriver.ChromeOptions()
    
    # Parâmetros para o ambiente Termux/Android
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-setuid-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.headless = False
    
    # Inicializa o driver
    service = Service("/usr/bin/chromedriver")
    driver = webdriver.Chrome(service=service, options=options)
    
    try:
        # Navega até o site
        driver.get("https://the-internet.herokuapp.com/login")
        
        # ESPERA EXPLÍCITA - Aguarda os elementos carregarem (até 10 segundos)
        wait = WebDriverWait(driver, 10)
        
        # Encontra e preenche o campo usuário
        username_field = wait.until(EC.visibility_of_element_located((By.ID, "username")))
        username_field.send_keys("tomsmith")
        
        # Encontra e preenche o campo senha
        password_field = wait.until(EC.visibility_of_element_located((By.ID, "password")))
        password_field.send_keys("SuperSecretPassword!")
        
        # Clica no botão de login
        login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
        login_button.click()
        
        # Verifica se o login foi bem sucedido
        wait.until(EC.url_contains("secure"))
#        assert "Secure Area" in driver.title
        # Verifica se a mensagem de sucesso aparece na página
        success_message = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "flash")))
        assert "secure" in success_message.text.lower()
        print("✅ Login realizado com sucesso! Mensagem:", success_message.text) 
        print("✅ Teste passou! Login realizado com sucesso!")
        
    finally:
        driver.quit()
