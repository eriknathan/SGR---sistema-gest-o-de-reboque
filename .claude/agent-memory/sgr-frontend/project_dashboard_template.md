---
name: Dashboard template
description: Estrutura, decisões de layout e padrões de componentes do core/dashboard.html
type: project
---

Template criado em `templates/core/dashboard.html`, estendendo `core/base.html`.

**Why:** Tarefa 2.2 do projeto SGR — tela inicial após login com visão geral operacional.

**How to apply:** Ao criar outras páginas de listagem/overview, seguir os mesmos padrões de card e tabela usados aqui.

## Estrutura

- Extends `core/base.html` (que inclui sidebar, topbar e messages via partials)
- Preenche `{% block page_title %}` com "Dashboard" para o topbar
- Todo o conteúdo dentro de `{% block content %}`

## Cards de Resumo

Grid: `grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6`

Cada card usa layout `flex items-center gap-5` com:
- Ícone SVG em container `w-12 h-12 rounded-xl` com fundo coral (`bg-[#e85d36]/10`) ou navy (`rgba(26,44,66,0.08)`) — alternados entre os 4 cards
- Valor numérico: `text-3xl font-bold text-[#1a2c42] leading-none`
- Label: `text-sm text-[#6b7280] mt-1.5`
- Fallback com filtro DTL: `{{ variavel|default:"0" }}`

Variáveis de contexto esperadas: `total_incidents`, `month_incidents`, `total_customers`, `total_drivers`

## Ícones SVG usados

- Total de Sinistros: ícone de documento (file-text)
- Sinistros do Mês: ícone de calendário
- Total de Clientes: ícone de grupo de pessoas (users)
- Motoristas Ativos: ícone de caminhão (truck)

## Tabela Últimos Sinistros

Variável de contexto: `recent_incidents` (lista dos 5 mais recentes)
Colunas: `#`, `Cliente`, `Motorista`, `Data`, `Status`
Campos acessados: `incident.id`, `incident.customer`, `incident.driver`, `incident.created_at|date:"d/m/Y"`, `incident.status`

Status badges mapeados:
- `concluded` → verde (`bg-green-100 text-green-800`)
- `in_progress` → amarelo (`bg-yellow-100 text-yellow-800`)
- `cancelled` → vermelho (`bg-red-100 text-red-800`)
- fallback/pendente → coral (`bg-[#e85d36]/10 text-[#e85d36]`)

Estado vazio tratado com `{% empty %}` — exibe "Nenhum sinistro registrado ainda." em `colspan="5"`.

## Decisão de background dos ícones navy

`bg-[#1a2c42]/8` não resolve corretamente no Tailwind CDN sem opacidade configurada. Solução aplicada: `style="background-color: rgba(26,44,66,0.08);"` inline nos cards de fundo navy para garantir renderização correta.
