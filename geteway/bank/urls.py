from django.urls import path
from . import views


app_name = 'bank'


urlpatterns = [
    path('page_1/', views.create_transaction, name='create_transaction'),
    path('page_2', views.confirm_transaction, name='confirm_transaction'),
    ]
