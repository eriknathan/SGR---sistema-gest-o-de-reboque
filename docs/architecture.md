# Arquitetura do Projeto

## Stack Técnica

| Camada | Tecnologia |
|---|---|
| Linguagem | Python 3.12+ |
| Framework Web | Django 5.x |
| Frontend | Django Template Language + TailwindCSS (CDN) |
| Banco de Dados | SQLite3 (inicial) → PostgreSQL (futuro) |
| Storage de Mídia | MinIO (Docker, local) → AWS S3 (futuro) |
| Geração de PDF | WeasyPrint ou ReportLab |
| E-mail | Django `send_mail` + SMTP via `.env` |
| Autenticação | Django nativo, customizado para login por e-mail |
| Config de Ambiente | `python-decouple` |
| API CNPJ | ReceitaWS ou BrasilAPI |
| API de CEP | ViaCEP |

## Estrutura de Apps

```
sgr/                        ← Projeto Django (settings, urls, wsgi)
├── accounts/               ← Autenticação customizada (login por e-mail)
├── customers/              ← Gestão de Clientes
├── drivers/                ← Gestão de Motoristas
├── fleet/                  ← Gestão de Frota
├── incidents/              ← Gestão de Sinistros (módulo central)
├── receipts/               ← Emissão de Recibos PDF
├── notifications/          ← Envio de E-mails
├── core/                   ← Mixins, helpers, views base (Dashboard)
└── templates/              ← Todos os templates HTML (raiz do projeto)
```

### Responsabilidade de Cada App

| App | Responsabilidade |
|---|---|
| `accounts` | `CustomUser` com login por e-mail, `EmailBackend` |
| `customers` | CRUD de clientes PF/PJ, integração ViaCEP e CNPJ API |
| `drivers` | CRUD de motoristas, histórico de pagamentos (`DriverPayment`) |
| `fleet` | CRUD de veículos da frota |
| `incidents` | Registro de sinistros, upload de fotos por etapa, UUID público |
| `receipts` | Geração de PDF A4, acesso público via UUID |
| `notifications` | Envio de e-mail com PDF anexado via SMTP |
| `core` | Dashboard, mixins compartilhados, templates base |

## Organização de Templates

Todos os templates ficam na pasta `templates/` na **raiz do projeto**, organizada por app:

```
templates/
├── core/
│   ├── base.html
│   ├── dashboard.html
│   ├── _sidebar.html
│   ├── _topbar.html
│   └── _messages.html
├── accounts/
├── customers/
├── drivers/
├── fleet/
├── incidents/
├── receipts/
└── notifications/
```

O `settings.py` aponta `DIRS` para esta pasta.

## Configurações Importantes (`settings.py`)

```python
AUTH_USER_MODEL = 'accounts.CustomUser'
AUTHENTICATION_BACKENDS = ['accounts.backends.EmailBackend']
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login/'
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
```
