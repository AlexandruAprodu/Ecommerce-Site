from django.db import models
from products.models import Products
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class OrderItem(models.Model):
    product = models.OneToOneField(Products, on_delete=models.SET_NULL, null=True)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(null=True)

    def __str__(self):
        return self.product.name


class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    shipping_address = models.TextField(default=None)
    invoice_address = models.TextField(default=None)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=False)


class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    shipped = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    date_ordered = models.DateTimeField(auto_now=True)
    shipping_address = models.ForeignKey(ShippingAddress, on_delete=models.PROTECT, null=True)

    def get_cart_items(self):
        return self.items.all()

    def get_cart_total(self):
        return sum([item.product.price for item in self.items.all()])

    def __str__(self):
        return f'{self.owner}'




