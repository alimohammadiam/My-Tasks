from django.shortcuts import render, redirect
from django.http import Http404
from .models import *
from .forms import *


# Create your views here.
def transaction(request):
    global amount, user_2, user_1
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            try:
                user_1 = Account.objects.get(account_number=form.account_number)
                user_2 = Account.objects.get(account_number=form.number_maghsad)
                amount = form.mablagh
            except:
                raise Http404('account number is invalid')

    else:
        form = TransactionForm()
    context = {
        'user_1': user_1.name,
        'user_2': user_2.name,
        'amount': amount
    }
    return render(request, "transaction_1.html", context)


