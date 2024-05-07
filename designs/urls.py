from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_designs, name='designs'),
    path('add/', views.add_design, name='add_design'),
    path('edit/<int:design_id>/', views.edit_design, name='edit_design'),
]