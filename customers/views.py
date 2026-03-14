"""Views for the customers app."""

import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import CustomerForm
from .models import Customer

logger = logging.getLogger(__name__)


class CustomerListView(LoginRequiredMixin, ListView):
    """
    Displays a paginated list of customers.

    Supports full-text search by name or document via the 'q' GET parameter.
    """

    model = Customer
    template_name = 'customers/customer_list.html'
    context_object_name = 'customers'
    paginate_by = 20

    def get_queryset(self):
        """Return customers filtered by the 'q' search parameter, if provided."""
        queryset = super().get_queryset()
        q = self.request.GET.get('q', '').strip()
        if q:
            queryset = queryset.filter(
                Q(name__icontains=q) | Q(document__icontains=q)
            )
        return queryset

    def get_context_data(self, **kwargs):
        """Add the current search query to the template context."""
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q', '')
        return context


class CustomerCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    Handles creation of a new Customer.

    Redirects to the customer list upon success and displays a confirmation message.
    """

    model = Customer
    form_class = CustomerForm
    template_name = 'customers/customer_form.html'
    success_url = reverse_lazy('customers:list')
    success_message = 'Cliente cadastrado com sucesso.'


class CustomerUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    Handles editing of an existing Customer.

    Redirects to the customer list upon success and displays a confirmation message.
    """

    model = Customer
    form_class = CustomerForm
    template_name = 'customers/customer_form.html'
    success_url = reverse_lazy('customers:list')
    success_message = 'Cliente atualizado com sucesso.'


class CustomerDetailView(LoginRequiredMixin, DetailView):
    """
    Displays the full profile of a single Customer.

    Attempts to load related incidents; silently ignores if the incidents
    app does not exist yet.
    """

    model = Customer
    template_name = 'customers/customer_detail.html'
    context_object_name = 'customer'

    def get_context_data(self, **kwargs):
        """
        Add related incidents to the context when the incidents app is available.

        Uses a try/except guard so this view works before the incidents app is created.
        """
        context = super().get_context_data(**kwargs)
        try:
            context['incidents'] = self.object.incident_set.all()
        except Exception:
            logger.debug(
                'incidents app not available yet — skipping incident_set lookup.'
            )
            context['incidents'] = []
        return context
