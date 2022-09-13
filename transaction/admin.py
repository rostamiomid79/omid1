from django.contrib import admin

from django.contrib import admin

from transaction.models import Transaction, UserBalance

@register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['user', 'amount', 'transaction_type', 'created_type']
    list_filter = ['transaction_type']
    search_fields = ['user__username']


@register(UserBalance)
class  UserBalanceAdmin(admin.ModelAdmin):
    list_display = ['user', 'balance', 'created_time']
    search_fields = ['user__username']