from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('logout', views.logout_view, name='logout'),
    path('accounts/profile/', views.accounts_profile, name='accounts_profile'),
    path('accounts/<int:pk>/', views.accounts_detail, name='accounts_detail'),
    path('main/', views.main, name='main'),
    path('nawa/', views.nawa, name='nawa'),
]