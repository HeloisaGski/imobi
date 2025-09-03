from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('imoveis/', views.property_list, name='property_list'),
    path('imovel/<int:pk>/', views.property_detail, name='property_detail'),
    path('empreendimentos/', views.development_list, name='development_list'),
]
