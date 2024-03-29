from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm    

def checkout(request):
    """
        A view to return the index page
    """

    quote = request.session.get('quote', {}) 
    if not quote:
        messages.error('There is no quote at the moment')
        return redirect(reverse('home'))

    form = OrderForm()

    template = 'checkout/checkout.html'
    
    context = {
        'form': form,
        'quote': quote,
    }

    return render(request, template, context)
