---
name: Customers app templates (Sprint 3)
description: Estrutura, decisões de layout, JS integrations e padrões dos templates da app customers criados na Sprint 3
type: project
---

## Templates criados

| Arquivo | Propósito |
|---|---|
| `templates/customers/customer_list.html` | Listagem paginada com busca via GET param `q` e badges PF/PJ |
| `templates/customers/customer_form.html` | Criação e edição — seções "Dados Gerais" e "Endereço", toggle PF/PJ, ViaCEP e CNPJ |
| `templates/customers/customer_detail.html` | Visualização completa com histórico de sinistros |

## Decisões de layout

- `customer_list.html`: tabela com `object_list` (padrão ListView do Django); paginação condicional via `page_obj`; estado vazio com mensagem contextual (distingue busca vazia de lista vazia).
- `customer_form.html`: único arquivo para create e edit — detecta edição via `{% if object %}`; formulário em dois cards separados (Dados Gerais / Endereço).
- `customer_detail.html`: avatar com inicial do nome gerado via `{{ customer.name|slice:':1'|upper }}`; endereço oculto atrás de condicional se todos os campos estiverem vazios.

## IDs de campo usados em JS (gerados automaticamente pelo Django)

| ID | Campo |
|---|---|
| `id_type` | select tipo PF/PJ |
| `id_document` | CPF / CNPJ |
| `id_name` | nome / razão social |
| `id_phone` | telefone |
| `id_email` | e-mail |
| `id_zip_code` | CEP |
| `id_street` | logradouro |
| `id_neighborhood` | bairro |
| `id_city` | cidade |
| `id_state` | UF |

## Integrações JS (customer_form.html — block extra_js)

- **Toggle PF/PJ**: função `applyTypeToggle(type)` chamada no `DOMContentLoaded` para suportar edição com valor pré-selecionado. Oculta/exibe `#cnpj-btn-wrapper` e altera placeholder de `id_document`.
- **ViaCEP**: função `buscarCep()` chamada pelo evento `blur` em `id_zip_code` (só se 8 dígitos) e pelo botão `#btn-buscar-cep` (tipo `button`, não submit).
- **BrasilAPI/CNPJ**: botão `#btn-buscar-cnpj` dentro de `#cnpj-btn-wrapper`; ao encontrar CNPJ, preenche nome, e-mail, telefone e, se `data.cep` existir, chama `buscarCep()` em cascata.

## Badges de tipo (lista e detalhe)

- PF: `bg-blue-100 text-blue-800`
- PJ: `bg-green-100 text-green-800`

## Badges de status de sinistro (customer_detail.html)

Mapeados pelos valores do campo `status` do model Incident:
- `completed` → verde
- `in_progress` → amarelo
- `cancelled` → vermelho
- default → coral (`bg-[#e85d36]/10 text-[#e85d36]`)

**Why:** Sprint 3 definiu os templates da app customers com foco em UX de cadastro rápido (autofill CEP/CNPJ) e listagem eficiente.
**How to apply:** Ao criar templates para outras apps (drivers, fleet, incidents), usar os mesmos padrões de seção de formulário, toggle de tipo, e estrutura de detalhe com histórico relacionado.
