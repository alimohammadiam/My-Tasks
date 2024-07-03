from django.contrib import admin
from .models import Transaction, Account
# Register your models here.


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'account_number', 'status']
    ordering = ['name', 'publish']
    list_filter = ['user', 'Balance', 'status']
    search_fields = ['name', 'user', 'account_number', 'phone_number']
    date_hierarchy = 'publish'
    list_editable = ['status']


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['user', 'transaction_status', 'amount', 'status', 'date_time']
    ordering = ['date_time']
    list_filter = ['date_time', 'transaction_status', 'status', 'amount']
    search_fields = ['user', 'amount', 'date_time']
    date_hierarchy = 'date_time'
    list_editable = ['status', 'transaction_status']

