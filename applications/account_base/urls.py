from django.urls import path
from . import views

app_name = 'account_base'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('accounts/login/', views.login_view, name='accounts-login'),
    path('logout/', views.logout_view, name='logout'),
]