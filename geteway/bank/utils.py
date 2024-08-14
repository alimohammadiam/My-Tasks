import random
import string
# from .models import Account


def create_account_number():
    prefix = '6037-9975'
    while True:
        from .models import Account
        middle = ''.join(random.choices(string.digits, k=6))
        account_number = f'{prefix}-{middle[:4]}-{middle[4:]}'
        if not Account.objects.filter(account_number=account_number).exists():
            break

    return account_number
