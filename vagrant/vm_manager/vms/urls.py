from django.urls import path
from .views import list_vms, manage_vm

urlpatterns = [
    path('list_vms/', list_vms, name='list_vms'),
    path('manage_vm/<str:action>/', manage_vm, name='manage_vm'),
]

