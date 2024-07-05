import decimal

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib import messages
from .models import Account, Transaction
from .forms import TransactionForm, ConfirmTransactionForm


# Create your views here.

def create_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            from_account_number = form.cleaned_data['from_account']
            to_account_number = form.cleaned_data['to_account']
            amount = form.cleaned_data['amount']

            from_account = get_object_or_404(Account, account_number=from_account_number)
            to_account = get_object_or_404(Account, account_number=to_account_number)

            if from_account.balance < amount:
                messages.error(request, 'موجودی ناکافی')
                return redirect('create_transaction')

            request.session['from_account'] = from_account.account_number
            request.session['to_account'] = to_account.account_number
            request.session['amount'] = str(amount)

            return redirect('confirm_transaction')

    else:
        form = TransactionForm()
    return render(request, 'create_transaction.html', {'form': form})


def confirm_transaction(request):
    from_account_number = request.session.get('from_account')
    to_account_number = request.session.get('to_account')
    amount = request.session.get('amount')

    if not from_account_number or not to_account_number or not amount:
        return redirect('bank:create_transaction')

    from_account = get_object_or_404(Account, account_number=from_account_number)
    to_account = get_object_or_404(Account, account_number=to_account_number)

    if request.method == 'POST':
        form = ConfirmTransactionForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            user = authenticate(username=from_account.user.username, password=password)

            if user is not None:
                from_account.balance -= decimal.Decimal(amount)
                to_account.balance += decimal.Decimal(amount)

                from_account.save()
                to_account.save()

                Transaction.objects.create(from_account=from_account, to_account=to_account, amount=amount)

                messages.success(request, 'تراکنش با موفقیت انجام شد')
                return redirect('bank:create_transaction')
            else:
                messages.error(request, 'رمز نادرست است')
    else:
        form = ConfirmTransactionForm()

    context = {
        'from_account': from_account,
        'to_account': to_account,
        'amount': amount,
        'form': form
    }
    return render(request, 'confirm_transaction.html', context)













