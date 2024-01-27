from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('register_user/', views.register_user, name='register_user'),
    path('login/', views.check, name='login'),
    path('login_user/', views.login_user, name='login_user'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_user, name='logout'),
]