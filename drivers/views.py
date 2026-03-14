"""Views for the drivers app."""

import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import DriverForm, DriverPaymentForm
from .models import Driver, DriverPayment

logger = logging.getLogger(__name__)


class DriverListView(LoginRequiredMixin, ListView):
    """List all drivers with optional search by name or document."""

    model = Driver
    template_name = 'drivers/driver_list.html'
    context_object_name = 'drivers'
    paginate_by = 20

    def get_queryset(self):
        """Return drivers filtered by search query if provided."""
        queryset = super().get_queryset()
        q = self.request.GET.get('q', '').strip()
        if q:
            queryset = queryset.filter(
                Q(name__icontains=q) | Q(document__icontains=q)
            )
        return queryset

    def get_context_data(self, **kwargs):
        """Add search query to context."""
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '')
        return context


class DriverCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """View for creating a new driver."""

    model = Driver
    form_class = DriverForm
    template_name = 'drivers/driver_form.html'
    success_url = reverse_lazy('drivers:list')
    success_message = 'Motorista cadastrado com sucesso.'


class DriverUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """View for updating an existing driver."""

    model = Driver
    form_class = DriverForm
    template_name = 'drivers/driver_form.html'
    success_url = reverse_lazy('drivers:list')
    success_message = 'Motorista atualizado com sucesso.'


class DriverDetailView(LoginRequiredMixin, DetailView):
    """View for displaying driver details, payments and related incidents."""

    model = Driver
    template_name = 'drivers/driver_detail.html'
    context_object_name = 'driver'

    def get_context_data(self, **kwargs):
        """Add payments and incidents to the context."""
        context = super().get_context_data(**kwargs)
        driver = self.object
        payments = driver.payments.all()
        context['payments'] = payments
        context['payments_total'] = sum(p.amount for p in payments)
        try:
            context['incidents'] = driver.incident_set.all()
        except Exception:
            logger.debug('incidents app not available yet; skipping incident_set lookup')
            context['incidents'] = []
        return context


class DriverPaymentCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """View for registering a new payment to a driver."""

    form_class = DriverPaymentForm
    template_name = 'drivers/payment_form.html'
    success_message = 'Pagamento registrado com sucesso.'

    def get_driver(self):
        """Return the driver instance from URL kwargs."""
        return get_object_or_404(Driver, pk=self.kwargs['driver_pk'])

    def form_valid(self, form):
        """Assign the driver to the payment before saving."""
        form.instance.driver = self.get_driver()
        return super().form_valid(form)

    def get_success_url(self):
        """Redirect to driver detail page after successful payment."""
        return reverse_lazy('drivers:detail', kwargs={'pk': self.kwargs['driver_pk']})

    def get_context_data(self, **kwargs):
        """Add the driver instance to the context."""
        context = super().get_context_data(**kwargs)
        context['driver'] = self.get_driver()
        return context
