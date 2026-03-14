---
name: project_core_app
description: App core criado na Sprint 2 — DashboardView com contexto defensivo via try/except para apps ainda não implementados
type: project
---

App `core` criado na Sprint 2 (2026-03-14) com a seguinte estrutura:

- `core/views.py` — `DashboardView(LoginRequiredMixin, TemplateView)` com `template_name = 'core/dashboard.html'`
- `core/urls.py` — `app_name = 'core'`, rota raiz `path('', DashboardView.as_view(), name='dashboard')`
- Registrado em `INSTALLED_APPS` como `'core.apps.CoreConfig'`
- Incluído em `sgr/urls.py` como `path('', include('core.urls', namespace='core'))`

**Padrão defensivo no `get_context_data`:** cada import de models de outros apps (`incidents`, `customers`, `drivers`) é feito dentro de `try/except Exception` com fallback para 0 / lista vazia. Isso permite que o dashboard funcione durante o desenvolvimento incremental por sprint.

**Why:** os apps `incidents`, `customers` e `drivers` ainda não existem na Sprint 2 — serão criados nas sprints 3-6.

**How to apply:** manter esse padrão até que todos os apps estejam implementados. Após implementação completa dos apps, os try/except podem ser removidos e os imports movidos para o topo do arquivo.
