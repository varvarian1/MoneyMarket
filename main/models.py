from django.db import models

# Create your models here.

class ExchangeRates(models.Model):
    Rub = models.CharField(max_length=255)
    Usdt = models.CharField(max_length=255)