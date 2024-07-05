from django import forms


class TransactionForm(forms.Form):
    from_account = forms.CharField(label='شماره حساب')
    to_account = forms.CharField(label='شماره حساب مقصد')
    amount = forms.DecimalField(max_digits=10, decimal_places=2, label='مبلغ')


class ConfirmTransactionForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput, label='رمز')

