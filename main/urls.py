from . import views
from django.urls import path

urlpatterns = [
    path('', views.long_running_task , name='long_running_task'),
]
