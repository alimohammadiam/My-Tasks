from django import forms
from captcha.fields import CaptchaField


class TransactionForm(forms.Form):
    from_account = forms.CharField(label='شماره حساب')
    to_account = forms.CharField(label='شماره حساب مقصد')
    amount = forms.DecimalField(max_digits=10, decimal_places=2, label='مبلغ')
    description = forms.CharField(max_length=250, required=False, label='توضیحات')


class ConfirmTransactionForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput, label='رمز')
    captcha = CaptchaField()

