from django import forms


class TransactionForm(forms.Form):
    account_number = forms.CharField(max_length=16, required=True)
    mablagh = forms.CharField(max_length=10, required=True)
    number_maghsad = forms.CharField(max_length=16, required=True)
