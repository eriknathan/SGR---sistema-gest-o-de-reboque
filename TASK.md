## Lista de Tarefas (Sprints)

---

### [x] 🏁 Sprint 0 — Setup e Configuração do Projeto

#### [x] Tarefa 0.1 — Inicialização do Projeto Django

- [x] **0.1.1** Criar o ambiente virtual Python (`python -m venv venv`).
- [x] **0.1.2** Instalar Django 5.x e dependências iniciais (`django`, `python-decouple`, `pillow`, `requests`).
- [x] **0.1.3** Criar o projeto Django com `django-admin startproject sgr .`.
- [x] **0.1.4** Criar o arquivo `.env` na raiz com as variáveis: `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`.
- [x] **0.1.5** Configurar `settings.py` para ler variáveis via `python-decouple`.
- [x] **0.1.6** Configurar `LANGUAGE_CODE = 'pt-br'` e `TIME_ZONE = 'America/Sao_Paulo'` no `settings.py`.
- [x] **0.1.7** Criar o arquivo `.gitignore` com entradas para `.env`, `venv/`, `*.sqlite3`, `__pycache__/`.
- [x] **0.1.8** Inicializar repositório Git e fazer commit inicial.

#### [x] Tarefa 0.2 — Configuração do TailwindCSS

- [x] **0.2.1** Adicionar o CDN do TailwindCSS ao template base com configuração de tema customizado (cores do Design System).
- [x] **0.2.2** Adicionar importação da fonte `Poppins` via Google Fonts no template base.
- [x] **0.2.3** Criar o arquivo `templates/base.html` com estrutura base: `<html>`, `<head>`, `<body>`, bloco `content`.

#### [x] Tarefa 0.3 — Estrutura de Templates

- [x] **0.3.1** Criar a pasta `templates/` na raiz do projeto.
- [x] **0.3.2** Configurar `DIRS` no `settings.py` para apontar para `templates/`.
- [x] **0.3.3** Criar subpastas: `templates/accounts/`, `templates/customers/`, `templates/drivers/`, `templates/fleet/`, `templates/incidents/`, `templates/receipts/`, `templates/core/`.
- [x] **0.3.4** Criar `templates/core/base.html` com layout padrão (sidebar + topbar + área de conteúdo).
- [x] **0.3.5** Criar `templates/core/_sidebar.html` como partial/include da sidebar.
- [x] **0.3.6** Criar `templates/core/_topbar.html` como partial/include da topbar.
- [x] **0.3.7** Criar `templates/core/_messages.html` como partial para exibir Django messages.

---

### [x] 🔐 Sprint 1 — Autenticação (accounts)

#### [x] Tarefa 1.1 — App de Autenticação

- [x] **1.1.1** Criar o app `accounts` com `python manage.py startapp accounts`.
- [x] **1.1.2** Registrar o app `accounts` em `INSTALLED_APPS` no `settings.py`.
- [x] **1.1.3** Criar modelo customizado `CustomUser` em `accounts/models.py` herdando de `AbstractUser`, substituindo `username` por `email` como campo de autenticação (`USERNAME_FIELD = 'email'`, `REQUIRED_FIELDS = []`).
- [x] **1.1.4** Configurar `AUTH_USER_MODEL = 'accounts.CustomUser'` no `settings.py`.
- [x] **1.1.5** Criar `accounts/backends.py` com `EmailBackend` para autenticação por e-mail.
- [x] **1.1.6** Configurar `AUTHENTICATION_BACKENDS` no `settings.py` para usar `EmailBackend`.
- [x] **1.1.7** Criar e aplicar migrations do app `accounts`.

#### [x] Tarefa 1.2 — Views e URLs de Login/Logout

- [x] **1.2.1** Criar `accounts/views.py` com `LoginView` customizada (CBV) usando `AuthenticationForm` adaptado para e-mail.
- [x] **1.2.2** Criar `accounts/forms.py` com `EmailAuthenticationForm` (campo `username` renomeado para `email`).
- [x] **1.2.3** Criar `accounts/urls.py` com rotas: `login/`, `logout/`.
- [x] **1.2.4** Incluir `accounts/urls.py` no `sgr/urls.py`.
- [x] **1.2.5** Configurar `LOGIN_URL`, `LOGIN_REDIRECT_URL` e `LOGOUT_REDIRECT_URL` no `settings.py`.

#### [x] Tarefa 1.3 — Templates de Autenticação

- [x] **1.3.1** Criar `templates/accounts/login.html` com layout centralizado, sem sidebar, com card de login.
- [x] **1.3.2** Aplicar Design System: fundo `#f8f9fb`, card branco com sombra, logo/título do sistema, campos de e-mail e senha com estilo padrão, botão CTA coral.
- [x] **1.3.3** Exibir mensagens de erro do formulário abaixo dos campos correspondentes.
- [x] **1.3.4** Adicionar `LoginRequiredMixin` a todas as views protegidas (será usado nas sprints seguintes).

---

### [x] 📊 Sprint 2 — Dashboard Principal (core)

#### [x] Tarefa 2.1 — App Core e Dashboard

- [x] **2.1.1** Criar o app `core` com `python manage.py startapp core`.
- [x] **2.1.2** Registrar o app em `INSTALLED_APPS`.
- [x] **2.1.3** Criar `core/views.py` com `DashboardView` (CBV, `LoginRequiredMixin`, `TemplateView`).
- [x] **2.1.4** Criar `core/urls.py` com rota `''` → `DashboardView`.
- [x] **2.1.5** Incluir `core/urls.py` no `sgr/urls.py` como rota raiz.

#### [x] Tarefa 2.2 — Template do Dashboard

- [x] **2.2.1** Criar `templates/core/dashboard.html` estendendo `base.html`.
- [x] **2.2.2** Criar seção de cards de resumo com: Total de Sinistros, Sinistros do Mês, Total de Clientes, Motoristas Ativos.
- [x] **2.2.3** Estilizar cards de resumo com ícone, valor em destaque e título, seguindo o Design System.
- [x] **2.2.4** Passar os dados dos cards via contexto na `DashboardView` (contagens via ORM do Django).
- [x] **2.2.5** Criar seção "Últimos Sinistros" com tabela dos 5 sinistros mais recentes.

---

### [x] 👥 Sprint 3 — Gestão de Clientes (customers)

#### [x] Tarefa 3.1 — Model de Cliente

- [x] **3.1.1** Criar o app `customers` com `python manage.py startapp customers`.
- [x] **3.1.2** Registrar o app em `INSTALLED_APPS`.
- [x] **3.1.3** Criar model `Customer` em `customers/models.py` com campos: `type` (PF/PJ), `name`, `document` (CPF/CNPJ), `phone`, `email`, `street`, `number`, `complement`, `neighborhood`, `city`, `state`, `zip_code`, `created_at`, `updated_at`.
- [x] **3.1.4** Criar e aplicar migrations do app `customers`.

#### [x] Tarefa 3.2 — Forms de Cliente

- [x] **3.2.1** Criar `customers/forms.py` com `CustomerForm` usando `ModelForm`.
- [x] **3.2.2** Aplicar classes do Design System (Tailwind) nos widgets dos campos via `attrs`.
- [x] **3.2.3** Tornar campos de endereço não obrigatórios no formulário.

#### [x] Tarefa 3.3 — Views e URLs de Cliente

- [x] **3.3.1** Criar `customers/views.py` com as CBVs: `CustomerListView`, `CustomerCreateView`, `CustomerUpdateView`, `CustomerDetailView`.
- [x] **3.3.2** Todas as views devem usar `LoginRequiredMixin`.
- [x] **3.3.3** `CustomerListView`: listar todos os clientes com busca por nome/documento via `GET` parameter.
- [x] **3.3.4** `CustomerCreateView`: salvar novo cliente com `success_message` e redirecionar para lista.
- [x] **3.3.5** `CustomerUpdateView`: editar cliente existente.
- [x] **3.3.6** `CustomerDetailView`: exibir dados do cliente e histórico de sinistros vinculados.
- [x] **3.3.7** Criar `customers/urls.py` com rotas: `''`, `create/`, `<pk>/edit/`, `<pk>/`.
- [x] **3.3.8** Incluir `customers/urls.py` no `sgr/urls.py` com prefixo `clientes/`.

#### [x] Tarefa 3.4 — Templates de Cliente

- [x] **3.4.1** Criar `templates/customers/customer_list.html` com tabela de clientes e barra de busca.
- [x] **3.4.2** Criar `templates/customers/customer_form.html` com formulário de criação/edição.
- [x] **3.4.3** Adicionar campo de CEP com botão "Buscar CEP" que faz fetch para ViaCEP via JavaScript e preenche os campos de endereço automaticamente.
- [x] **3.4.4** Adicionar campo de CNPJ com botão "Buscar CNPJ" que faz fetch para API de CNPJ via JavaScript para clientes PJ.
- [x] **3.4.5** Criar `templates/customers/customer_detail.html` com dados do cliente e tabela de histórico de sinistros.
- [x] **3.4.6** Adicionar toggle de tipo (PF/PJ) que exibe/oculta campos correspondentes via JavaScript.

---

### [x] 🚗 Sprint 4 — Gestão de Motoristas (drivers)

#### [x] Tarefa 4.1 — Model de Motorista

- [x] **4.1.1** Criar o app `drivers` com `python manage.py startapp drivers`.
- [x] **4.1.2** Registrar o app em `INSTALLED_APPS`.
- [x] **4.1.3** Criar model `Driver` com campos: `name`, `document` (CPF), `phone`, `email`, `cnh_number`, `cnh_category`, `cnh_expiration`, `admission_date`, `base_salary`, campos de endereço, `created_at`, `updated_at`.
- [x] **4.1.4** Criar model `DriverPayment` com campos: `driver` (FK), `amount`, `payment_date`, `description`, `created_at`, `updated_at`.
- [x] **4.1.5** Criar e aplicar migrations do app `drivers`.

#### [x] Tarefa 4.2 — Forms de Motorista

- [x] **4.2.1** Criar `drivers/forms.py` com `DriverForm` e `DriverPaymentForm`.
- [x] **4.2.2** Aplicar classes do Design System nos widgets.

#### [x] Tarefa 4.3 — Views e URLs de Motorista

- [x] **4.3.1** Criar CBVs: `DriverListView`, `DriverCreateView`, `DriverUpdateView`, `DriverDetailView`.
- [x] **4.3.2** `DriverDetailView`: incluir histórico de pagamentos no contexto.
- [x] **4.3.3** Criar view para adicionar pagamento ao motorista.
- [x] **4.3.4** Criar `drivers/urls.py` e incluir no `sgr/urls.py` com prefixo `motoristas/`.

#### [x] Tarefa 4.4 — Templates de Motorista

- [x] **4.4.1** Criar `templates/drivers/driver_list.html`.
- [x] **4.4.2** Criar `templates/drivers/driver_form.html` com CEP autocomplete via ViaCEP.
- [x] **4.4.3** Criar `templates/drivers/driver_detail.html` com dados completos e histórico de pagamentos.

---

### [x] 🚛 Sprint 5 — Gestão de Frota (fleet)

#### [x] Tarefa 5.1 — Model de Veículo

- [x] **5.1.1** Criar o app `fleet` com `python manage.py startapp fleet`.
- [x] **5.1.2** Registrar o app em `INSTALLED_APPS`.
- [x] **5.1.3** Criar model `Vehicle` com campos: `model`, `brand`, `plate`, `renavam`, `year`, `color`, `type`, `created_at`, `updated_at`.
- [x] **5.1.4** Criar e aplicar migrations do app `fleet`.

#### [x] Tarefa 5.2 — Forms, Views e URLs de Frota

- [x] **5.2.1** Criar `fleet/forms.py` com `VehicleForm`.
- [x] **5.2.2** Criar CBVs: `VehicleListView`, `VehicleCreateView`, `VehicleUpdateView`, `VehicleDetailView`.
- [x] **5.2.3** Criar `fleet/urls.py` e incluir no `sgr/urls.py` com prefixo `frota/`.

#### [x] Tarefa 5.3 — Templates de Frota

- [x] **5.3.1** Criar `templates/fleet/vehicle_list.html` com busca por placa.
- [x] **5.3.2** Criar `templates/fleet/vehicle_form.html`.
- [x] **5.3.3** Criar `templates/fleet/vehicle_detail.html`.

---

### ⚡ Sprint 6 — Gestão de Sinistros (incidents)

#### Tarefa 6.1 — Models de Sinistro

- [ ] **6.1.1** Criar o app `incidents` com `python manage.py startapp incidents`.
- [ ] **6.1.2** Registrar o app em `INSTALLED_APPS`.
- [ ] **6.1.3** Criar model `Incident` com todos os campos descritos no ERD (FK para Customer, Driver, Vehicle; dados do veículo rebocado, trajeto, financeiro, data/hora, observações, UUID).
- [ ] **6.1.4** Criar model `IncidentPhoto` com campos: `incident` (FK), `photo_url`, `stage` (choices: BEFORE, EMBARKED, DELIVERED), `created_at`, `updated_at`.
- [ ] **6.1.5** Configurar geração automática de UUID no model `Incident` usando `uuid.uuid4`.
- [ ] **6.1.6** Criar e aplicar migrations do app `incidents`.

#### Tarefa 6.2 — Forms de Sinistro

- [ ] **6.2.1** Criar `incidents/forms.py` com `IncidentForm`.
- [ ] **6.2.2** Implementar campo de `service_value` com conversão automática para extenso ao salvar (usando biblioteca `num2words` com locale `pt_BR`).
- [ ] **6.2.3** Criar `IncidentPhotoForm` para upload de fotos por etapa.

#### Tarefa 6.3 — Views e URLs de Sinistro

- [ ] **6.3.1** Criar CBV `IncidentListView` com filtro por cliente, motorista e data.
- [ ] **6.3.2** Criar CBV `IncidentCreateView` com lógica para cadastro inline de cliente (via modal ou redirect).
- [ ] **6.3.3** Criar CBV `IncidentUpdateView`.
- [ ] **6.3.4** Criar CBV `IncidentDetailView` com dados completos, fotos e ações (emitir PDF, enviar e-mail).
- [ ] **6.3.5** Criar view de upload de fotos por etapa (`IncidentPhotoUploadView`).
- [ ] **6.3.6** Criar `incidents/urls.py` e incluir no `sgr/urls.py` com prefixo `sinistros/`.

#### Tarefa 6.4 — Templates de Sinistro

- [ ] **6.4.1** Criar `templates/incidents/incident_list.html` com filtros e tabela.
- [ ] **6.4.2** Criar `templates/incidents/incident_form.html` com selects encadeados e atalho para novo cliente.
- [ ] **6.4.3** Criar `templates/incidents/incident_detail.html` com seções: dados gerais, veículo rebocado, trajeto, financeiro, fotos, ações.
- [ ] **6.4.4** Criar seção de upload de fotos com visualização das imagens enviadas por etapa.
- [ ] **6.4.5** Implementar preview de imagens ao selecionar arquivo no input de upload.

---

### 📄 Sprint 7 — Emissão de Recibos PDF (receipts)

#### Tarefa 7.1 — App de Recibos

- [ ] **7.1.1** Criar o app `receipts` com `python manage.py startapp receipts`.
- [ ] **7.1.2** Registrar o app em `INSTALLED_APPS`.
- [ ] **7.1.3** Instalar biblioteca de geração de PDF (`WeasyPrint` ou `ReportLab`).
- [ ] **7.1.4** Criar model `Receipt` com campos: `incident` (FK OneToOne), `file_name`, `file_path`, `generated_at`, `created_at`, `updated_at`.
- [ ] **7.1.5** Criar e aplicar migrations.

#### Tarefa 7.2 — Geração do PDF

- [ ] **7.2.1** Criar `receipts/utils.py` com função `generate_receipt_pdf(incident)` que gera o PDF com layout A4.
- [ ] **7.2.2** Criar template HTML do recibo: `templates/receipts/receipt_pdf.html` com cabeçalho (dados da empresa), corpo (dados do sinistro, veículo, trajeto, valor em extenso) e rodapé (assinatura digital).
- [ ] **7.2.3** Implementar nomenclatura do arquivo: `Recibo-[NomeDaEmpresa]-[Placa]-[Data].pdf`.
- [ ] **7.2.4** Salvar o arquivo gerado no diretório `MEDIA_ROOT/receipts/`.
- [ ] **7.2.5** Registrar o recibo gerado na model `Receipt`.

#### Tarefa 7.3 — Views de Recibo

- [ ] **7.3.1** Criar view `GenerateReceiptView` (POST) que chama `generate_receipt_pdf` e redireciona para detalhe do sinistro com mensagem de sucesso.
- [ ] **7.3.2** Criar view `PublicReceiptView` que exibe o recibo via UUID, sem necessidade de login, acessível publicamente.
- [ ] **7.3.3** Criar `receipts/urls.py` com rotas: `gerar/<int:incident_pk>/`, `visualizar/<uuid:uuid>/`.
- [ ] **7.3.4** Incluir `receipts/urls.py` no `sgr/urls.py`.

#### Tarefa 7.4 — Template de Visualização Pública

- [ ] **7.4.1** Criar `templates/receipts/receipt_public.html` para exibição pública do recibo sem sidebar.
- [ ] **7.4.2** Adicionar botão "Imprimir" ou "Salvar PDF" na visualização pública.

---

### 📧 Sprint 8 — Envio de E-mail (notifications)

#### Tarefa 8.1 — App de Notificações

- [ ] **8.1.1** Criar o app `notifications` com `python manage.py startapp notifications`.
- [ ] **8.1.2** Registrar o app em `INSTALLED_APPS`.
- [ ] **8.1.3** Configurar variáveis de e-mail no `.env`: `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, `EMAIL_USE_TLS`, `DEFAULT_FROM_EMAIL`.
- [ ] **8.1.4** Configurar `EMAIL_BACKEND` e variáveis no `settings.py` via `python-decouple`.

#### Tarefa 8.2 — Lógica de Envio

- [ ] **8.2.1** Criar `notifications/utils.py` com função `send_receipt_email(incident, receipt)`.
- [ ] **8.2.2** Criar template HTML do e-mail: `templates/notifications/email_receipt.html` com logo, resumo do serviço, link público UUID e assinatura.
- [ ] **8.2.3** Implementar lógica de anexo do PDF ao e-mail via `EmailMessage` do Django.
- [ ] **8.2.4** Tratar exceções de envio com try/except e retornar sucesso/falha.

#### Tarefa 8.3 — View de Envio Rápido

- [ ] **8.3.1** Criar view `SendReceiptEmailView` (POST) na tela de detalhe do sinistro.
- [ ] **8.3.2** Chamar `send_receipt_email` e exibir mensagem de sucesso/erro via Django messages.
- [ ] **8.3.3** Criar URL para envio de e-mail e adicionar ao `notifications/urls.py`.
- [ ] **8.3.4** Incluir `notifications/urls.py` no `sgr/urls.py`.

---

### ⚙️ Sprint 9 — Configurações e Finalizações

#### Tarefa 9.1 — Página de Configurações

- [ ] **9.1.1** Criar view e template `templates/core/settings.html` para configurações do sistema.
- [ ] **9.1.2** Adicionar informações sobre a empresa (nome, CNPJ, endereço, logo) lidas via `.env` e exibidas no painel.
- [ ] **9.1.3** Exibir status da configuração SMTP (conectado/desconectado).

#### Tarefa 9.2 — Ajustes Finais de UX

- [ ] **9.2.1** Garantir que todas as páginas de listagem tenham paginação (`Paginator` do Django).
- [ ] **9.2.2** Implementar sidebar responsiva com toggle hamburguer para mobile.
- [ ] **9.2.3** Revisar todos os formulários para garantir feedback de erro em português.
- [ ] **9.2.4** Adicionar favicon ao sistema (baseado na identidade visual).
- [ ] **9.2.5** Verificar e corrigir todos os redirecionamentos pós-ação (salvar, excluir, enviar).
- [ ] **9.2.6** Adicionar `404.html` e `500.html` customizados com o Design System.

#### Tarefa 9.3 — Revisão de Código e Qualidade

- [ ] **9.3.1** Revisar todos os arquivos `.py` para conformidade com PEP8 (usar `flake8`).
- [ ] **9.3.2** Adicionar docstrings a todas as classes e métodos.
- [ ] **9.3.3** Verificar uso de aspas simples em todo o código Python.
- [ ] **9.3.4** Validar que todos os models possuem `created_at` e `updated_at`.
- [ ] **9.3.5** Confirmar que todos os signals estão em arquivos `signals.py` dos respectivos apps.

---

### 🐳 Sprint 10 — Docker e Testes _(Sprints Finais)_

#### Tarefa 10.1 — Docker

- [ ] **10.1.1** Criar `Dockerfile` para a aplicação Django.
- [ ] **10.1.2** Criar `docker-compose.yml` com serviços: `web` (Django), `minio` (storage de fotos).
- [ ] **10.1.3** Configurar variáveis de ambiente no `docker-compose.yml` via arquivo `.env`.
- [ ] **10.1.4** Testar build e funcionamento completo do sistema via Docker.

#### Tarefa 10.2 — Testes Automatizados

- [ ] **10.2.1** Configurar `pytest-django` e `factory-boy`.
- [ ] **10.2.2** Escrever testes unitários para models (criação, validação, campos obrigatórios).
- [ ] **10.2.3** Escrever testes de integração para views (login, CRUD de clientes, criação de sinistro).
- [ ] **10.2.4** Escrever testes para geração de PDF e envio de e-mail (mocks).
- [ ] **10.2.5** Configurar cobertura de código e atingir mínimo de 70% de cobertura.

---
