from django.urls import path

from .views import (CurrenciesListView,
                    CurrencyCreateView,
                    CurrencyCalculator,
                    CurrencyCalculatorView)

app_name = 'calculator'

urlpatterns = [
    path('', CurrenciesListView.as_view(), name='currencies'),
    path('currency/add', CurrencyCreateView.as_view(), name='add_currency'),
    path('currency_calculator/', CurrencyCalculatorView.as_view(),
        name='currency_calculator'),
    path('ajax_calcalate/', CurrencyCalculator.as_view(),
        name='ajax_calcalate'),
]
