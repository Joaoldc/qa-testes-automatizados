import pytest
from pages.login_page import LoginPage

class TestLoginValido:
    """Testes de login com credenciais corretas"""
    
    def test_login_com_sucesso(self, driver):
        """Teste tradicional sem Page Object (para comparação)"""
        # Arrange
        login_page = LoginPage(driver)
        login_page.open()
        
        # Act
        login_page.do_login("tomsmith", "SuperSecretPassword!")
        
        # Assert
        assert login_page.is_login_successful()
        assert "secure" in login_page.get_flash_message().lower()
        print("\n✅ Login válido funcionou!")
    
    def test_login_com_sucesso_usando_fixture(self, login_page):
        """Teste usando fixture (código ainda mais limpo)"""
        # Act
        login_page.do_login("tomsmith", "SuperSecretPassword!")
        
        # Assert
        assert login_page.is_login_successful()
        print("\n✅ Login válido (com fixture) funcionou!")
