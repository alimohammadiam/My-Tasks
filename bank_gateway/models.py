from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Account(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DR', 'Draft'
        PUBLISHED = 'PB', 'Published'
        REJECT = 'RJ', 'reject'

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_account')
    name = models.CharField(max_length=250)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    phone_number = models.CharField(max_length=11, unique=True)
    account_number = models.CharField(max_length=16, unique=True)
    Balance = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    address = models.TextField()

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish'])
        ]

    def __str__(self):
        return self.name


class Transaction(models.Model):
    class TransactionType(models.TextChoices):
        DEPOSIT = 'DE', 'Deposit'
        WITHDRAW = 'WI', 'withdraw'
        BALANCE_INQUIRY = 'BI', 'Balance_inquiry'

    transaction_type = models.CharField(max_length=2, choices=TransactionType.choices,
                                        default=TransactionType.BALANCE_INQUIRY)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transaction')
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='transaction_account')
    description = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['-date_time']
        indexes = [
            models.Index(fields=['-date_time'])
        ]

    def __str__(self):
        return f'{self.account.name} - {self.transaction_type} - {self.amount}'

