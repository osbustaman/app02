from django.urls import path
from . import views

app_name = 'base_app'

urlpatterns = [
    path('control-panel/', views.controlPanel, name='controlPanel'),

]