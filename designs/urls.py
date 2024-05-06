from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_designs, name='designs'),
    path('add/', views.add_design, name='add_design'),
]