# Design System

## Paleta de Cores

| Token | Hex | Uso |
|---|---|---|
| `navy-primary` | `#1a2c42` | Sidebar, cabeçalhos, texto principal |
| `navy-light` | `#264060` | Hover states, navegação secundária |
| `coral-primary` | `#e85d36` | Botões de ação principal (CTAs), destaques |
| `coral-light` | `#ed7d5e` | Hover de botões e links em destaque |
| `coral-dark` | `#d64821` | Active states (botões clicados) |
| `bg-app` | `#f8f9fb` | Fundo geral da aplicação |
| `card-bg` | `#ffffff` | Fundo de cards e containers |
| `text-muted` | `#6b7280` | Legendas, placeholders, textos secundários |

## Tipografia

- **Família:** `Poppins` (Google Fonts)
- **Pesos:** 300, 400, 500, 600, 700

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
```

## Configuração do Tailwind (CDN)

```html
<script>
  tailwind.config = {
    theme: {
      extend: {
        colors: {
          'navy': { 'primary': '#1a2c42', 'light': '#264060' },
          'coral': { 'primary': '#e85d36', 'light': '#ed7d5e', 'dark': '#d64821' },
          'app': { 'bg': '#f8f9fb', 'card': '#ffffff', 'muted': '#6b7280' }
        },
        fontFamily: { 'sans': ['Poppins', 'sans-serif'] }
      }
    }
  }
</script>
```

## Layout Base

Sidebar fixa (264px) à esquerda + área de conteúdo principal com topbar.

```html
<body class="bg-[#f8f9fb] font-sans">
  <aside class="fixed inset-y-0 left-0 w-64 bg-[#1a2c42] text-white flex flex-col z-50">
    <!-- Logo -->
    <div class="px-6 py-5 border-b border-[#264060]">
      <span class="text-xl font-bold text-white tracking-wide">SGR</span>
    </div>
    <!-- Nav -->
    <nav class="flex-1 px-3 py-4 space-y-1">
      <!-- item inativo -->
      <a href="#" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-sm font-medium
                         text-white/70 hover:bg-[#264060] hover:text-white transition-all">
        <!-- ícone + label -->
      </a>
      <!-- item ativo -->
      <a href="#" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-sm font-medium
                         bg-[#e85d36] text-white">
        <!-- ícone + label -->
      </a>
    </nav>
  </aside>

  <main class="ml-64 min-h-screen">
    <header class="bg-white border-b border-gray-200 px-6 py-4 flex items-center justify-between">
      <h1 class="text-lg font-semibold text-[#1a2c42]">Título da Página</h1>
    </header>
    <div class="p-6"><!-- conteúdo --></div>
  </main>
</body>
```

Em mobile, a sidebar é ocultada e exibida via toggle hamburguer no topbar.

## Componentes

### Card

```html
<div class="bg-white rounded-xl shadow-sm border border-gray-100 p-6">
  <h2 class="text-base font-semibold text-[#1a2c42] mb-4">Título</h2>
</div>
```

### Botões

```html
<!-- Primário -->
<button class="inline-flex items-center gap-2 px-4 py-2.5 bg-[#e85d36] hover:bg-[#ed7d5e]
               active:bg-[#d64821] text-white text-sm font-medium rounded-lg transition-colors">
  Ação Principal
</button>

<!-- Secundário -->
<button class="inline-flex items-center gap-2 px-4 py-2.5 bg-white hover:bg-gray-50
               border border-gray-200 text-[#1a2c42] text-sm font-medium rounded-lg transition-colors">
  Ação Secundária
</button>

<!-- Perigo -->
<button class="inline-flex items-center gap-2 px-4 py-2.5 bg-red-600 hover:bg-red-700
               text-white text-sm font-medium rounded-lg transition-colors">
  Excluir
</button>
```

### Inputs

```html
<div class="space-y-1.5">
  <label class="block text-sm font-medium text-[#1a2c42]">Label</label>
  <input type="text"
         class="w-full px-3 py-2.5 text-sm bg-white border border-gray-200 rounded-lg
                text-[#1a2c42] placeholder-[#6b7280]
                focus:outline-none focus:ring-2 focus:ring-[#e85d36]/30 focus:border-[#e85d36]
                transition-colors">
</div>

<!-- Mensagem de erro -->
<p class="text-xs text-red-500 mt-1">Este campo é obrigatório.</p>
```

### Tabelas

```html
<div class="bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden">
  <table class="min-w-full divide-y divide-gray-100">
    <thead class="bg-[#f8f9fb]">
      <tr>
        <th class="px-4 py-3 text-left text-xs font-semibold text-[#6b7280] uppercase tracking-wider">
          Coluna
        </th>
      </tr>
    </thead>
    <tbody class="divide-y divide-gray-100">
      <tr class="hover:bg-gray-50 transition-colors">
        <td class="px-4 py-3.5 text-sm text-[#1a2c42]">Valor</td>
      </tr>
    </tbody>
  </table>
</div>
```

### Badges de Status

```html
<!-- Verde -->
<span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-green-100 text-green-800">Concluído</span>
<!-- Amarelo -->
<span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-yellow-100 text-yellow-800">Em Andamento</span>
<!-- Vermelho -->
<span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-red-100 text-red-800">Cancelado</span>
<!-- Coral -->
<span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-[#e85d36]/10 text-[#e85d36]">Pendente</span>
```

### Mensagens de Feedback (Django Messages)

```html
{% if messages %}
  {% for message in messages %}
    <div class="px-4 py-3 rounded-lg text-sm font-medium mb-4
                {% if message.tags == 'success' %}bg-green-50 text-green-800 border border-green-200
                {% elif message.tags == 'error' %}bg-red-50 text-red-800 border border-red-200
                {% elif message.tags == 'warning' %}bg-yellow-50 text-yellow-800 border border-yellow-200
                {% else %}bg-blue-50 text-blue-800 border border-blue-200{% endif %}">
      {{ message }}
    </div>
  {% endfor %}
{% endif %}
```

## Responsividade

- **Mobile First:** grids com `grid-cols-1 md:grid-cols-2 lg:grid-cols-3`.
- Sidebar ocultada em mobile, exibida via toggle no topbar.
