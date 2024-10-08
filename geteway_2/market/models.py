from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    product_name = models.CharField(max_length=250)
    product_price = models.CharField(max_length=20)
    quantity = models.IntegerField(default=1)

    def total_price(self):
        return self.product_price * self.quantity