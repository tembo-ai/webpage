from django.urls import path
from initial_test import views

urlpatterns = [
    path('', views.initial_test, name='initial_test'),
]
