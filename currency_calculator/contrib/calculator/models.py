from django.db import models


class Currency(models.Model):
    currency_name = models.CharField(max_length=50, blank=False, null=False)
    currency_code = models.CharField(max_length=3, unique=True, blank=False, null=False)
    currency_value = models.FloatField(blank=False, null=False)
    currency_unit = models.FloatField(blank=False, null=False)
    currency_unification_unit =  models.FloatField(blank=False, null=False)
    def __str__(self):
        return '{}'.format(self.currency_name)

class CurrencyProxy(Currency):
    class Meta:
        proxy = True
        auto_created = True
        
    def get_currency_unit(self):
        return float(self.currency_value / self.currency_unit)