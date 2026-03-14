"""URL configuration for the drivers app."""

from django.urls import path

from .views import (
    DriverCreateView,
    DriverDetailView,
    DriverListView,
    DriverPaymentCreateView,
    DriverUpdateView,
)

app_name = 'drivers'

urlpatterns = [
    path('', DriverListView.as_view(), name='list'),
    path('create/', DriverCreateView.as_view(), name='create'),
    path('<int:pk>/edit/', DriverUpdateView.as_view(), name='edit'),
    path('<int:pk>/', DriverDetailView.as_view(), name='detail'),
    path('<int:driver_pk>/payment/add/', DriverPaymentCreateView.as_view(), name='payment_add'),
]
