from django.urls import path

from .views import VehicleCreateView, VehicleDetailView, VehicleListView, VehicleUpdateView

app_name = 'fleet'

urlpatterns = [
    path('', VehicleListView.as_view(), name='list'),
    path('create/', VehicleCreateView.as_view(), name='create'),
    path('<int:pk>/edit/', VehicleUpdateView.as_view(), name='edit'),
    path('<int:pk>/', VehicleDetailView.as_view(), name='detail'),
]
