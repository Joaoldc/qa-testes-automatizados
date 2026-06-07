from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    """Page Object para a página de login"""
    
    # Localizadores dos elementos (centralizados e fáceis de manter)
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH_MESSAGE = (By.CLASS_NAME, "flash")
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def open(self):
        """Abre a página de login"""
        self.driver.get("https://the-internet.herokuapp.com/login")
        return self
    
    def fill_username(self, username):
        """Preenche o campo de usuário"""
        element = self.wait.until(EC.visibility_of_element_located(self.USERNAME_INPUT))
        element.clear()
        element.send_keys(username)
        return self
    
    def fill_password(self, password):
        """Preenche o campo de senha"""
        element = self.wait.until(EC.visibility_of_element_located(self.PASSWORD_INPUT))
        element.clear()
        element.send_keys(password)
        return self
    
    def click_login(self):
        """Clica no botão de login"""
        element = self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON))
        element.click()
        return self
    
    def do_login(self, username, password):
        """Método combinado para fazer login completo"""
        self.fill_username(username)
        self.fill_password(password)
        self.click_login()
        return self
    
    def get_flash_message(self):
        """Retorna o texto da mensagem de flash (sucesso/erro)"""
        element = self.wait.until(EC.visibility_of_element_located(self.FLASH_MESSAGE))
        return element.text
    
    def is_login_successful(self):
        """Verifica se o login foi bem sucedido"""
        try:
            message = self.get_flash_message()
            return "secure" in message.lower()
        except:
            return False
    
    def get_error_message(self):
        """Retorna a mensagem de erro específica"""
        message = self.get_flash_message()
        return message
