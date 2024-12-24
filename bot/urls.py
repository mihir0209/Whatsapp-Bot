# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('incoming/', views.incoming_message, name='incoming_message'),
]
