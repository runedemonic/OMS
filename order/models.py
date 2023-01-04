from django.db import models
from django.conf import settings
# Create your models here.
class Order(models.Model):
    company_name = models.CharField(max_length=100)
    product_name = models.CharField(max_length=200)
    product_code = models.CharField(max_length=100, blank=True)
    price = models.IntegerField()
    quantity = models.IntegerField()
    sum = models.IntegerField()
    order_date = models.DateField(auto_now=True)
    due_date = models.DateField(blank=True)
