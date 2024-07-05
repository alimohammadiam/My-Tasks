from django.contrib import admin
from .models import Transaction, Account

# Register your models here.


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['user', 'account_number', "balance"]
    ordering = ['account_number']
    list_filter = ['user', 'account_number', "balance"]
    search_fields = ['user', 'account_number', "balance"]
    readonly_fields = ['account_number']


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['from_account', 'to_account', 'amount', 'date']
    ordering = ['date']
    list_filter = ['from_account', 'to_account', 'amount']
    search_fields = ['from_account', 'to_account', 'amount', 'date']