
import requests
from lxml import html
from django.core.management.base import BaseCommand

from currency_calculator.contrib.calculator.models import Currency, CurrencyProxy


class Command(BaseCommand):
    def handle(self, *args, **options):
        url = 'http://bnb.bg/Statistics/StExternalSector/StExchangeRates/StERForeignCurrencies/index.htm'
        response = requests.get(url)
        htmldata = html.fromstring(response.content)
        tbody = htmldata.xpath('//*[@id="Exchange_Rate_Search"]/div[1]/table/tbody/tr/td/text()')
        values = [tbody[x:x+5] for x in range(0, len(tbody), 5)]

        for a in values:
            Currency.objects.update_or_create(
                currency_code=a[1],
                defaults={'currency_name': a[0],
                          'currency_unit': a[2],
                          'currency_value': a[3],
                          'currency_unification_unit': float(a[3])/float(a[2])
                          }
            )
        

        