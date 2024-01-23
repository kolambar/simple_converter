from rest_framework.views import APIView

from converter.models import ExchangeRate
from converter.services import get_rate
from rest_framework.response import Response

from converter.utils import shorten_time


class GetExchangeRate(APIView):

    def get(self, request):
        instance = get_rate()

        # Последние 10 запросов, без самого нового
        history_of_last_ten_requests = ExchangeRate.objects.order_by('-time')[1:11]

        # Вернуть объект модели в виде ответа JSON
        return Response({
            f'{shorten_time(instance.time)}, {instance.currency_to_sale}:{instance.currency_to_buy}':
                instance.rate,
            'last 10 requests':
                ((obj.rate, shorten_time(obj.time)) for obj in history_of_last_ten_requests)
        })
