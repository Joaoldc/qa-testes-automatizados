'''import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

def test_login_visual_firefox():
    # 1. Configura as opções do Firefox
    options = Options()
    
    # IMPORTANTE: Mantém o navegador visível na sua tela X11
    options.headless = False 

    # 2. Inicializa o driver apontando para o Geckodriver nativo do Debian
    service = Service("/usr/local/bin/geckodriver")
    driver = webdriver.Firefox(service=service, options=options)
    
    try:
        # 3. Abre o site de testes no Firefox
      #  driver.get("herokuapp.com")
        driver.get("https://the-internet.herokuapp.com")
        time.sleep(8) # Pausa para você ver o Firefox abrindo no tablet

        # 4. Preenche os campos do formulário
        driver.find_element(By.ID, "username").send_keys("tomsmith")
        driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        time.sleep(8)

        # 5. Clica no botão de Login
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(8) # Pausa para carregar a página interna

        # 6. Validação de QA (Asserção)
        mensagem_sucesso = driver.find_element(By.ID, "flash").text
        assert "You logged into a secure area!" in mensagem_sucesso

        # 7. Tira um print de evidência
        driver.save_screenshot("evidencia_firefox_x11.png")
        print("\n[QA] Teste executado com sucesso no Firefox!")

    finally:
        # 8. Fecha o navegador de forma limpa
        driver.quit()
'''

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_visual_firefox():
    # Configura o navegador Firefox
    options = webdriver.FirefoxOptions()
    options.headless = False
    
    # Inicializa o driver (ajuste o caminho se necessário)
    service = Service("/usr/local/bin/geckodriver")
    driver = webdriver.Firefox(service=service, options=options)
    
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
