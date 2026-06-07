import pytest
from pages.login_page import LoginPage

class TestLoginInvalido:
    """Testes de login com credenciais incorretas"""
    
    # Dados parametrizados para testar vários cenários de erro
    @pytest.mark.parametrize("username,password,expected_error", [
        ("usuario_errado", "SuperSecretPassword!", "Your username is invalid!"),
        ("tomsmith", "senha_errada", "Your password is invalid!"),
        ("", "SuperSecretPassword!", "Your username is invalid!"),
        ("tomsmith", "", "Your password is invalid!"),
        ("", "", "Your username is invalid!"),
    ])
    def test_login_com_credenciais_invalidas(self, driver, username, password, expected_error):
        """Testa vários cenários de login inválido"""
        # Arrange
        login_page = LoginPage(driver)
        login_page.open()
        
        # Act
        login_page.do_login(username, password)
        
        # Assert
        assert not login_page.is_login_successful()
        assert expected_error in login_page.get_flash_message()
        print(f"\n❌ Login inválido correto! Mensagem: {login_page.get_flash_message()}")
    
    def test_login_com_usuario_inexistente(self, login_page):
        """Teste específico: usuário que não existe"""
        # Act
        login_page.do_login("usuariofake123", "qualquersenha")
        
        # Assert
        assert "Your username is invalid!" in login_page.get_flash_message()
        assert not login_page.is_login_successful()
        print("\n❌ Usuário inexistente detectado corretamente!")
    
    def test_login_com_senha_vazia(self, login_page):
        """Teste específico: senha em branco"""
        # Act
        login_page.do_login("tomsmith", "")
        
        # Assert
        assert "Your password is invalid!" in login_page.get_flash_message()
        print("\n❌ Senha vazia detectada corretamente!")
    
    def test_login_campos_em_branco(self, login_page):
        """Teste específico: campos completamente vazios"""
        # Act
        login_page.do_login("", "")
        
        # Assert
        assert "Your username is invalid!" in login_page.get_flash_message()
        print("\n❌ Campos vazios detectados corretamente!")
