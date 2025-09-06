from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('imoveis/', views.property_list, name='property_list'),
    path('imovel/<int:pk>/', views.property_detail, name='property_detail'),
    path('empreendimentos/', views.development_list, name='development_list'),
    path('newsletter/', views.newsletter_signup, name='newsletter_signup'),

    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    path('profile/', views.profile, name='profile'),
    path('toggle_favorite/', views.toggle_favorite, name='toggle_favorite'),
]
