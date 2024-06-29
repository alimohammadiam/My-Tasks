from django.contrib import admin
from .models import Transaction
# Register your models here.


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['user', 'transaction_type', 'amount', 'status', 'date_time']
    ordering = ['date_time']
    list_filter = ['date_time', 'transaction_type', 'status', 'amount']
    search_fields = ['user', 'amount', 'date_time']
    date_hierarchy = 'date_time'
    list_editable = ['status', 'transaction_type']

