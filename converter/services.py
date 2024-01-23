from datetime import datetime, timedelta

import requests
import xml.etree.ElementTree as ET

from converter.models import ExchangeRate


def get_rate() -> ExchangeRate:
    """
    Получает объект модели ExchangeRate со стоимостью USD в рублях
    :return ExchangeRate:
    """
    currency_to_exchange = 'USD'  # Валюта для сравнения с рублями (USD)
    now = datetime.now()
    last_rate = ExchangeRate.objects.first()  # Последний записанный курс из базы данных

    # Если прошло менее 1 дня с записи последнего курса, возвращаем курс из базы данных
    if last_rate.time.replace(tzinfo=None) - now < timedelta(days=1):
        exchange_rate = last_rate
    # Иначе получаем курс по API и записываем в базу данных
    else:
        rate = float(
            ET.fromstring(requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text)
            .find(f'./Valute[CharCode="{currency_to_exchange}"]/Value')  # Находим тег Value с нужным кодом валюты
            .text.replace(',', '.')  # Заменить запятую на точку
        )
        exchange_rate = ExchangeRate.objects.create(
            rate=rate
        )

    return exchange_rate
