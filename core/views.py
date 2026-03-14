from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class DashboardView(LoginRequiredMixin, TemplateView):
    """View principal do dashboard do SGR.

    Exibe cards com totais de sinistros, clientes e motoristas.
    Imports dos apps ainda não implementados são feitos com try/except
    para permitir desenvolvimento incremental por sprint.
    """

    template_name = 'core/dashboard.html'

    def get_context_data(self, **kwargs):
        """Monta o contexto do dashboard com totais e lista de sinistros recentes.

        Usa try/except em cada import para que o dashboard funcione mesmo
        quando os apps incidents, customers e drivers ainda não existem.
        """
        context = super().get_context_data(**kwargs)

        try:
            from incidents.models import Incident
            from django.utils import timezone
            now = timezone.now()
            context['total_incidents'] = Incident.objects.count()
            context['month_incidents'] = Incident.objects.filter(
                created_at__year=now.year,
                created_at__month=now.month,
            ).count()
            context['recent_incidents'] = Incident.objects.select_related(
                'customer', 'driver'
            ).order_by('-created_at')[:5]
        except Exception:
            context['total_incidents'] = 0
            context['month_incidents'] = 0
            context['recent_incidents'] = []

        try:
            from customers.models import Customer
            context['total_customers'] = Customer.objects.count()
        except Exception:
            context['total_customers'] = 0

        try:
            from drivers.models import Driver
            context['total_drivers'] = Driver.objects.count()
        except Exception:
            context['total_drivers'] = 0

        return context
