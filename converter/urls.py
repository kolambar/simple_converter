from django.urls import path

from converter.apps import ConverterConfig
from converter.views import GetExchangeRate

app_name = ConverterConfig.name

urlpatterns = [
    path('get-current-usd/', GetExchangeRate.as_view(), name='exchange_rate'),
]
