# Setup e Desenvolvimento

## Pré-requisitos

- Python 3.12+
- Git

## Instalação

```bash
# 1. Clonar o repositório
git clone <url-do-repo>
cd sgr

# 2. Criar e ativar ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# 3. Instalar dependências
pip install django python-decouple pillow requests num2words

# 4. Configurar variáveis de ambiente
cp .env.example .env
# Editar .env com os valores corretos
```

## Variáveis de Ambiente (`.env`)

```env
# Django
SECRET_KEY=sua-secret-key-aqui
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# E-mail (SMTP)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=seu@email.com
EMAIL_HOST_PASSWORD=sua-senha
EMAIL_USE_TLS=True
DEFAULT_FROM_EMAIL=seu@email.com

# Dados da Empresa (usados nos recibos)
COMPANY_NAME=Nome da Empresa
COMPANY_CNPJ=00.000.000/0000-00
COMPANY_ADDRESS=Endereço da Empresa
```

## Rodando o Projeto

```bash
# Aplicar migrations
python manage.py migrate

# Criar superusuário
python manage.py createsuperuser

# Iniciar servidor de desenvolvimento
python manage.py runserver
```

Acesse em `http://localhost:8000`.

## Estrutura de Sprints

O desenvolvimento é organizado em sprints conforme `TASK.md`:

| Sprint | Foco |
|---|---|
| 0 | Setup do projeto, TailwindCSS, estrutura de templates |
| 1 | Autenticação com login por e-mail (`accounts`) |
| 2 | Dashboard principal (`core`) |
| 3 | Gestão de Clientes (`customers`) |
| 4 | Gestão de Motoristas (`drivers`) |
| 5 | Gestão de Frota (`fleet`) |
| 6 | Gestão de Sinistros (`incidents`) |
| 7 | Emissão de Recibos PDF (`receipts`) |
| 8 | Envio de E-mail (`notifications`) |
| 9 | Configurações, UX e revisão de código |
| 10 | Docker e testes automatizados |

## Qualidade de Código

```bash
# Verificar conformidade com PEP8
pip install flake8
flake8 .
```

Meta de cobertura de testes: **70%** mínimo (Sprint 10), usando `pytest-django` e `factory-boy`.

## Docker (Sprint 10)

```bash
docker-compose up --build
```

Serviços: `web` (Django) + `minio` (storage de fotos).
