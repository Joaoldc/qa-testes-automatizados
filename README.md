# QA Web Tests

Automação de testes funcionais para o site [The Internet](https://the-internet.herokuapp.com) utilizando **Selenium WebDriver** + **pytest**, com foco na página de login.

Functional test automation for [The Internet](https://the-internet.herokuapp.com) using **Selenium WebDriver** + **pytest**, focused on the login page.

---

## Estrutura do Projeto

```
qa-web-tests/
├── conftest.py              # Fixtures do pytest (driver, login_page)
├── test_selenium.py         # Testes com Chrome
├── test_firefox.py          # Testes com Firefox
├── pages/
│   ├── login_page.py        # Page Object da página de login
│   └── __init__.py
└── tests/
    ├── test_login_valido.py     # Testes de login com credenciais corretas
    ├── test_login_invalido.py   # Testes de login com credenciais inválidas
    └── __init__.py
```

---

## Tecnologias

- **Python 3**
- **Selenium WebDriver**
- **pytest**
- **Page Object Model**
- **ChromeDriver** & **GeckoDriver**

---

## Instalação

```bash
# Clone o repositório
git clone https://github.com/Joaoldc/qa-testes-automatizados.git
cd qa-web-tests

# Crie e ative um virtual environment
python3 -m venv venv
source venv/bin/activate  # Linux/macOS

# Instale as dependências
pip install selenium pytest
```

**Pré-requisitos:** ChromeDriver e/ou GeckoDriver instalados e acessíveis nos caminhos configurados em `conftest.py`.

---

## Como Executar

```bash
# Todos os testes
pytest -v

# Testes específicos
pytest tests/test_login_valido.py -v
pytest tests/test_login_invalido.py -v
pytest test_selenium.py -v
pytest test_firefox.py -v

# Com output detalhado
pytest -v --tb=short
```

---

## Testes

### Login Válido
- `test_login_com_sucesso` — Login com credenciais corretas (Page Object)
- `test_login_com_sucesso_usando_fixture` — Mesmo teste usando fixture do pytest

### Login Inválido (dados parametrizados)
- Usuário errado / senha correta
- Usuário correto / senha errada
- Campos vazios (combinações)

### Login Inválido (casos específicos)
- `test_login_com_usuario_inexistente`
- `test_login_com_senha_vazia`
- `test_login_campos_em_branco`

---

## Page Object Model

A classe `LoginPage` encapsula todos os localizadores e interações da página de login:

```python
login_page = LoginPage(driver)
login_page.open()
login_page.do_login("tomsmith", "SuperSecretPassword!")
assert login_page.is_login_successful()
```

---

## Fixtures

O arquivo `conftest.py` fornece duas fixtures:

- **`driver`** — Inicializa e finaliza o ChromeDriver para cada teste
- **`login_page`** — Retorna a `LoginPage` já com a página aberta

---

## Observações

- Os testes utilizam **esperas explícitas** (`WebDriverWait`) para maior confiabilidade
- Desenvolvido e testado em ambiente **Termux/Android** com parâmetros `--no-sandbox` e `--disable-dev-shm-usage`
- Sistema Ubunto proot, instalado via termux, criando um ambiente posível para desenvolver e testar sistemas em um tablet Android utilizando algumas ferramentas de desenvolvimento compatível com essa arquitetura.
- Compatível com Chrome e Firefox
