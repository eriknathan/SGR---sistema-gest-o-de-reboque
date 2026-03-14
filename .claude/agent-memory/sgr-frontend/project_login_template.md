---
name: login_template
description: Decisões de implementação e estrutura do template de login do SGR
type: project
---

O template de login está em `templates/accounts/login.html` e estende `base.html` (raiz), não `core/base.html`.

**Why:** A página de login não tem sidebar nem topbar. `base.html` expõe `{% block layout %}` que por padrão contém apenas `{% block content %}`, permitindo layout full-page sem sidebar. `core/base.html` sobrescreve `{% block layout %}` incluindo sidebar e topbar — não deve ser usado no login.

**How to apply:** Qualquer template de página pública (login, acesso por UUID, etc.) deve estender `base.html` diretamente e sobrescrever `{% block content %}`. Templates autenticados devem estender `core/base.html`.

Detalhes do layout do login:
- Fundo: o `<body>` em `base.html` já tem `bg-[#f8f9fb]`; o wrapper usa `min-h-screen flex items-center justify-center`
- Logo "SGR": `text-4xl font-bold text-[#1a2c42]` (navy sobre fundo claro, NÃO branco)
- Card: `bg-white rounded-2xl shadow-xl p-8`, largura `max-w-sm`
- Erros `non_field_errors`: bloco `bg-red-50 border border-red-200` acima do formulário
- Erros de campo: `<p class="text-xs text-red-500 mt-1">` abaixo do input, com `border-red-400` no input
- Botão submit: `w-full inline-flex items-center justify-center` com classes CTA coral padrão
