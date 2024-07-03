from django.urls import path
from . import views

app_name = 'bank_gateway'


urlpatterns = [
    path('', views.Transaction, name='log_in'),
]