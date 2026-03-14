# SGR — Agentes de IA

Agentes especializados na stack do projeto para uso com Claude Code.

## Índice

| Agente | Arquivo | Especialidade |
|---|---|---|
| [Backend](#backend) | `backend.md` | Django 5.x — models, views, forms, signals, PDF, e-mail |
| [Frontend](#frontend) | `frontend.md` | Django Templates + TailwindCSS — componentes, JS inline |
| [QA](#qa) | `qa.md` | Testes no navegador via Playwright — fluxos e visual |

---

## Backend

**Arquivo:** `backend.md`

Engenheiro backend especializado em Django 5.x. Responsável por toda a lógica Python do projeto.

**Use este agente para:**
- Criar ou alterar models, migrations, forms, views (CBV), URLs e signals
- Implementar autenticação customizada por e-mail (`accounts`)
- Escrever lógica de geração de PDF (WeasyPrint/ReportLab) e envio de e-mail (SMTP)
- Integrar APIs externas: ViaCEP, CNPJ (BrasilAPI), MinIO
- Configurar `settings.py`, variáveis de ambiente e `urls.py`

**Não use para:** templates HTML, CSS, JavaScript

**MCP:** Context7 — consulta documentação de `django`, `python-decouple`, `weasyprint`, `num2words`

---

## Frontend

**Arquivo:** `frontend.md`

Engenheiro frontend especializado em Django Template Language e TailwindCSS via CDN.

**Use este agente para:**
- Criar ou modificar templates HTML em qualquer app (`templates/<app>/`)
- Implementar componentes do Design System (cards, tabelas, botões, badges, formulários)
- Escrever JavaScript inline: busca ViaCEP, busca CNPJ, preview de upload, toggle da sidebar mobile
- Garantir responsividade Mobile First e consistência visual

**Não use para:** código Python, models, views, lógica de negócio

**MCP:** Context7 — consulta documentação de `tailwindcss` e `django` (template tags, filtros, paginação)

---

## QA

**Arquivo:** `qa.md`

Testador que acessa o sistema rodando localmente via Playwright e verifica funcionamento e visual.

**Use este agente para:**
- Testar fluxos completos: login, CRUD, upload de fotos, geração de PDF, envio de e-mail
- Validar aplicação do Design System (cores, tipografia, layout)
- Verificar responsividade em viewport mobile (375px)
- Identificar erros, bugs visuais e comportamentos inesperados

**Pré-requisito:** o sistema deve estar rodando em `http://localhost:8000`

**MCP:** Playwright — navegação, cliques, preenchimento de formulários, screenshots

---

## Fluxo de Trabalho

```
Tarefa de backend  →  agente: backend  →  escreve Python
Tarefa de UI/HTML  →  agente: frontend →  escreve templates
Validar o sistema  →  agente: qa       →  testa no navegador
```

Para tarefas que envolvem backend e frontend juntos (ex: criar um CRUD completo), acione o `backend` primeiro para criar models/views, depois o `frontend` para criar os templates.
