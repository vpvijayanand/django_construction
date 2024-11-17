from django.urls import path
from . import views  # Import views from your app

urlpatterns = [
    path('', views.welcome, name='welcome'),  # Add this URL pattern
]
