from django.db import models


class ExchangeRate(models.Model):
    rate = models.FloatField()
    currency_to_sale = models.CharField(max_length=3, default='USD')
    currency_to_buy = models.CharField(max_length=3, default='RUB')
    time = models.DateTimeField(auto_now=True)
