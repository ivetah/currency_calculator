from django.core import management
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, View, TemplateView

from .models import Currency
from .forms import CurrencyForm
from currency_calculator.contrib.base.mixins import AjaxRequestMixin
# Create your views here.


class CurrenciesListView(ListView):
    template_name = 'currencies.html'
    model = Currency

    def dispatch(self, request, *args, **kwargs):
        if 'sync' in request.GET:
            management.call_command("sync_currencies")

        return super().dispatch(request, *args, **kwargs)


class CurrencyCreateView(CreateView):
    form_class = CurrencyForm
    template_name = 'create.html'
    model = Currency
    success_url = reverse_lazy('calculator:currencies')


class CurrencyCalculatorView(TemplateView):
    template_name = 'calculator.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['currencies'] = (Currency.objects.all()
            .values('currency_code', 'currency_name'))

        return context

class CurrencyCalculator(AjaxRequestMixin, View):

    def post(self, request, *args, **kwargs):
        value = float(request.POST.get('value', None))

        from_c = request.POST.get('from_c', 'BGN')
        to_c = request.POST.get('to_c', 'BGN')
        lv_1 = lv_2 = value
        
        if from_c != 'BGN':
            lv_1 = (Currency.objects.get(currency_code=from_c)
                                      .currency_unification_unit)
        
        if to_c != 'BGN':
            lv_2 = (Currency.objects.get(currency_code=to_c)
                            .currency_unification_unit)
 
        result = "{:.4f}".format((lv_1*value)/lv_2)
        data = {'result': result}

        return JsonResponse(data)

    

