from . models import ExchangeRates
from django.forms import ModelForm, TextInput

class ExchangeRatesForm(ModelForm):
    class Meta:
        model = ExchangeRates
        fields = ['Rub', 'Usdt']

        widgets = {
            'Rub': TextInput(attrs={
                'placeholder': 'Enter RUB'
            }),
            'Usdt': TextInput(attrs={
                'placeholder': 'Enter BAHT'
            })            
        }