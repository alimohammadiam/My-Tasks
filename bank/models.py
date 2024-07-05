from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from .utils import create_account_number
import uuid

# Create your models here.


class Account(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DR', 'Draft'
        PUBLISHED = 'PB', 'Published'
        REJECTED = 'RJ', 'Rejected'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=20, unique=True, default=create_account_number, editable=False)
    balance = models.DecimalField(max_digits=15, decimal_places=2, validators=[MinValueValidator(0.0)])
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)

    class Meta:
        ordering = ['-create_time']
        indexes = [
            models.Index(fields=['-create_time'])
        ]

    def __str__(self):
        return f'Account ({self.user.username} - {self.account_number})'


class Transaction(models.Model):
    from_account = models.ForeignKey(Account, related_name='outgoing_transactions', on_delete=models.CASCADE)
    to_account = models.ForeignKey(Account, related_name='incoming_transactions', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    is_successful = models.BooleanField(default=False)
    transaction_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    description = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        ordering = ['-date']
        indexes = [
            models.Index(fields=['-date'])
        ]

    def __str__(self):
        return f'Transaction ID : {self.transaction_id}'

