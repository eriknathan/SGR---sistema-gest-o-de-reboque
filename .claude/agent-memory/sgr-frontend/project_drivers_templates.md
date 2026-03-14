---
name: Drivers templates (Sprint 4)
description: driver_list, driver_form, driver_detail e payment_form — IDs de campo JS, alerta de CNH, badges de categoria e total de pagamentos
type: project
---

Quatro templates criados em `templates/drivers/` na Sprint 4.

**Why:** App `drivers` gerencia motoristas e seus pagamentos; CNH vencida é informação crítica operacionalmente.

**How to apply:** Consultar estes padrões ao estender ou criar views do app `drivers`.

## Arquivos

- `templates/drivers/driver_list.html`
- `templates/drivers/driver_form.html`
- `templates/drivers/driver_detail.html`
- `templates/drivers/payment_form.html`

## Padrões e decisões

### Alerta de CNH (driver_list e driver_detail)
- Implementado em JS puro no bloco `{% block extra_js %}`.
- Lê o atributo `data-expiration="YYYY-MM-DD"` em cada célula/span com classe `.cnh-expiration-cell`.
- Vencida (< hoje): texto vermelho + badge "Vencida" (bg-red-100/text-red-700).
- Vencendo em 30 dias: texto amarelo + badge "Vence em breve" (bg-yellow-100/text-yellow-700).
- Não usa filtros DTL de data comparativa — toda lógica no cliente para evitar necessidade de tag customizada.

### Badges de categoria CNH
Mapeamento de cor por categoria (consistente em list e detail):
- A → blue-100/blue-800
- B → green-100/green-800
- AB → purple-100/purple-800
- C → yellow-100/yellow-800
- D → [#e85d36]/10 / [#e85d36] (coral)
- E → red-100/red-800

### ViaCEP (driver_form)
- IDs padrão do Django: `id_zip_code`, `id_street`, `id_neighborhood`, `id_city`, `id_state`.
- Função `buscarCep()` compartilhada entre evento `blur` no campo CEP e botão "Buscar CEP" (`id="btn-buscar-cep"`).
- Sem integração CNPJ — motoristas são sempre PF.

### Histórico de Pagamentos (driver_detail)
- Contexto esperado da view: `payments` (queryset de DriverPayment) e `payments_total` (valor agregado sum).
- Rodapé da tabela (`<tfoot>`) exibe `payments_total` formatado com `floatformat:2`.
- Botão "Registrar Pagamento" aponta para `{% url 'drivers:payment_add' driver.pk %}`.

### payment_form
- Formulário `DriverPaymentForm` com campos: `amount`, `payment_date`, `description`.
- `driver` disponível no contexto — usado no subtítulo e nos links de cancelar/voltar.
- Largura máxima `max-w-2xl` (formulário simples, não precisa de grid completo).

### base.html real
- O `core/base.html` real estende `base.html` e usa blocos `{% block layout %}`, `{% block page_title %}` e `{% block topbar_actions %}`.
- Templates de app estendem `core/base.html` (não `base.html` diretamente).
- Mensagens são incluídas via `{% include 'core/_messages.html' %}` dentro do próprio `core/base.html` — os templates de app não precisam repeti-las.
