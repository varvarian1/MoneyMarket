from django.shortcuts import render, redirect
from . models import ExchangeRates
from . forms import ExchangeRatesForm

# Create your views here.

def index_main(request):

    exchange = ExchangeRates.objects.all()

    if request.method == 'POST':
        form = ExchangeRatesForm(request.POST)
        if form.is_valid():

            Rub = form.cleaned_data['Rub']
            Usdt = form.cleaned_data['Usdt']

            exchange_rates = ExchangeRates.objects.first()
            exchange_rates.Rub = Rub
            exchange_rates.Usdt = Usdt
            exchange_rates.save()

            return redirect('main')
    else:
        form = ExchangeRatesForm

    return render(request, 'main/index.html', {'form': form, 'exchange': exchange})

