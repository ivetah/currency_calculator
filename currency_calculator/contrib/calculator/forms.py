from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, ButtonHolder, Submit, Div

from .models import Currency


class CurrencyForm(forms.ModelForm):
    currency_name = forms.CharField(
        required=True,
        label='Name',
        widget=forms.TextInput(
            attrs={}
        )
    )
    currency_code = forms.CharField(
        required=True,
        label='Code',
        widget=forms.TextInput()
    )
    currency_unit = forms.FloatField(
        required=True,
        label='For unit currency',
        widget=forms.NumberInput(
            attrs={}
        )
    )
    currency_value = forms.FloatField(
        required=True,
        label='Value',
        widget=forms.NumberInput(
            attrs={}
        )
    )
    currency_unification_unit = forms.FloatField(
        required=False,
        label='',
        widget=forms.NumberInput(
            attrs={
                'style': 'display: none;'
            }
        )
    )
   
    class Meta:
        model = Currency
        fields = [
            'currency_name',
            'currency_code',
            'currency_unit',
            'currency_value',
            'currency_unification_unit'
        ]

    def __init__(self, *args, **kwargs):
        super(CurrencyForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(Column('currency_name', css_class='form-group col-6'),
                Column('currency_code', css_class='form-group col-6')),
            Row(Column('currency_value', css_class='form-group col-6'),
                Column('currency_unit', css_class='form-group col-6')),
            'currency_unification_unit',
            Div(ButtonHolder(Submit('submit', 
                'Add', css_class='btn btn-primary pull-right'),
                       css_class='card-footer')
            )
            
        )
    
    def clean(self):
        cleaned_data = super().clean()
        cleaned_data['currency_unification_unit'] = cleaned_data['currency_value']/cleaned_data['currency_unit']
        return cleaned_data