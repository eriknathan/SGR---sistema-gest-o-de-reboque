import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import VehicleForm
from .models import Vehicle

logger = logging.getLogger(__name__)


class VehicleListView(LoginRequiredMixin, ListView):
    """List all vehicles with optional search by plate, brand or model."""

    model = Vehicle
    template_name = 'fleet/vehicle_list.html'
    context_object_name = 'vehicles'
    paginate_by = 20

    def get_queryset(self):
        """Return vehicles filtered by search query when provided."""
        queryset = super().get_queryset()
        query = self.request.GET.get('q', '').strip()
        if query:
            queryset = queryset.filter(
                Q(plate__icontains=query)
                | Q(brand__icontains=query)
                | Q(model__icontains=query)
            )
        return queryset

    def get_context_data(self, **kwargs):
        """Add search query to context for template rendering."""
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context


class VehicleCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """Create a new vehicle in the fleet."""

    model = Vehicle
    form_class = VehicleForm
    template_name = 'fleet/vehicle_form.html'
    success_url = reverse_lazy('fleet:list')
    success_message = 'Veículo cadastrado com sucesso.'


class VehicleUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """Update an existing vehicle in the fleet."""

    model = Vehicle
    form_class = VehicleForm
    template_name = 'fleet/vehicle_form.html'
    success_url = reverse_lazy('fleet:list')
    success_message = 'Veículo atualizado com sucesso.'


class VehicleDetailView(LoginRequiredMixin, DetailView):
    """Display detailed information for a single vehicle."""

    model = Vehicle
    template_name = 'fleet/vehicle_detail.html'
    context_object_name = 'vehicle'

    def get_context_data(self, **kwargs):
        """Add related incidents to context if the incidents app is available."""
        context = super().get_context_data(**kwargs)
        try:
            context['incidents'] = self.object.incident_set.all()
        except Exception:
            logger.debug('incidents app not available yet — skipping related incidents.')
            context['incidents'] = []
        return context
