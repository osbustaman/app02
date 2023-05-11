from django.urls import path

from applications.base.views import controlPanel

app_name = 'base_app'

urlpatterns = [
    path('control-panel/', controlPanel, name='control-panel'),
]