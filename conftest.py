import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture
def driver():
    """Fixture que fornece um driver do Chrome para cada teste"""
    options = webdriver.ChromeOptions()
    
    # Configurações para ambiente Termux/Android
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-setuid-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.headless = False
    
    service = Service("/usr/bin/chromedriver")
    driver = webdriver.Chrome(service=service, options=options)
    
    yield driver  # Fornece o driver para o teste
    
    # Código executado após o teste (sempre fecha o navegador)
    driver.quit()

@pytest.fixture
def login_page(driver):
    """Fixture que já retorna a LoginPage aberta"""
    from pages.login_page import LoginPage
    page = LoginPage(driver)
    page.open()
    return page
