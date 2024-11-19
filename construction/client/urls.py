from django.urls import path
from . import views

urlpatterns = [
    path('clients/', views.client_list, name='client-list'),            # List all clients
    path('clients/create/', views.client_create, name='client-create'), # Create a new client
    path('clients/update/<int:id>/', views.client_update, name='client-update'), # Update a client by ID
    path('clients/delete/<int:id>/', views.client_delete, name='client-delete'), # Delete a client by ID
]
