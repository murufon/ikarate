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
    path('sample/', views.sample, name='sample'),
    path('boshuuran/', views.boshuuran, name='boshuuran'),
    path('boshuu/', views.boshuu, name='boshuu'),

    # Twitter
    path('authorization/twitter_login/', views.twitter_login, name='twitter_login'),
    path('authorization/twitter_callback/', views.twitter_callback, name='twitter_callback'),
    path('authorization/twitter_logout/', views.twitter_logout, name='twitter_logout'),
]

