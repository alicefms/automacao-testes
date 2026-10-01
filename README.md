# Automação de Testes Web

Projeto de automação de testes web para o SauceDemo, desenvolvido com Python 3.14, Selenium WebDriver, pytest e Guará. A automação usa o padrão Page Transactions para separar a interação com a interface dos cenários de teste.

## Cenários

- Login bem-sucedido.
- Rejeição de credenciais inválidas e de usuário bloqueado.
- Fluxo de compra de um produto, do login à confirmação do pedido.
- Envio de formulário de demonstração do Selenium, marcado como teste de integração externa.

## Estrutura

```text
tests/
├── conftest.py                 # Fixtures compartilhadas do pytest
├── fixtures/
│   └── driver.py               # Criação e encerramento do Chrome WebDriver
├── pages/                      # Seletores, interações e esperas por página
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── confirmation_page.py
│   └── selenium_form_page.py
├── specs/                      # Cenários e assertions do pytest
│   ├── test_login.py
│   ├── test_checkout.py
│   └── test_selenium_form.py
├── transactions/
│   └── app_transactions.py     # Ações executadas pela Application do Guará
└── settings.py                 # URL base e dados de teste
```

As pages encapsulam os localizadores e as esperas explícitas do Selenium. As transactions representam ações do usuário e delegam a interação às pages. Os specs organizam os cenários e verificam os resultados. A fixture encerra o navegador mesmo quando um teste falha.

## Pré-requisitos

- Python 3.14.
- Google Chrome instalado.
- Git.

O Selenium inicia o Chrome pelo WebDriver. As dependências Python do projeto estão declaradas em `requirements.txt`.

## Instalação

### Windows PowerShell

Na raiz do repositório:

```powershell
py -3.14 -m venv .venv
\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Se o PowerShell bloquear a ativação do ambiente, permita scripts somente na sessão atual e tente ativar novamente:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
\.venv\Scripts\Activate.ps1
```

### Ubuntu / Linux

Na raiz do repositório:

```bash
python3.14 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Executar os testes

Ative o ambiente virtual e execute os comandos a partir da raiz do projeto.

Rodar todos os testes:

```bash
python -m pytest tests/
```

Rodar somente os testes essenciais marcados como `smoke`:

```bash
python -m pytest tests/ -m smoke
```

Rodar o teste de integração com o formulário externo:

```bash
python -m pytest tests/ -m integration
```

Rodar um arquivo específico:

```bash
python -m pytest tests/specs/test_login.py
```

As markers disponíveis estão declaradas em `pytest.ini`. Atualmente, `smoke` identifica os cenários essenciais de login e compra; `integration` identifica o teste que acessa o site de demonstração do Selenium.

## Relatórios

O plugin `pytest-html` está incluído em `requirements.txt`. Crie a pasta de saída e execute:

PowerShell:

```powershell
New-Item -ItemType Directory -Force reports | Out-Null
python -m pytest tests/ --html=reports/report.html --junitxml=reports/results.xml --self-contained-html
```

Ubuntu / Linux:

```bash
mkdir -p reports
python -m pytest tests/ --html=reports/report.html --junitxml=reports/results.xml --self-contained-html
```

Os arquivos gerados são `reports/report.html` e `reports/results.xml`. Para gerar relatórios somente dos testes smoke, acrescente `-m smoke` ao comando.

## URL da aplicação

A aplicação padrão é `https://www.saucedemo.com/`. É possível sobrescrevê-la com a variável de ambiente `BASE_URL`.

PowerShell:

```powershell
$env:BASE_URL = "https://www.saucedemo.com/"
```

Ubuntu / Linux:

```bash
export BASE_URL="https://www.saucedemo.com/"
```

## GitHub Actions

O workflow em `.github/workflows/tests.yml` roda no Ubuntu quando há `push` ou `pull_request` para `main`. Ele configura Python 3.14, instala o Chrome e as dependências, executa os testes `smoke` e publica os relatórios como artefato `automation-reports`. O teste marcado como `integration` não é executado por esse workflow atualmente.
