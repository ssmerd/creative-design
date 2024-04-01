from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm    

def checkout(request):
    """
        A view to return the index page
    """

    stripe_public_key = 'pk_live_51P0kUf2MqiGwcstyNOY8fysCeHRmBWkNlxiETVhKHWgOZE23DFawGXqnwHJLp4InQjsXmqNqzNhovytucKZXw91200cqNVfTsb'
    stripe_secret_key = 'test'

    quote = request.session.get('quote', {}) 
    if not quote:
        messages.error('There is no quote at the moment')
        return redirect(reverse('home'))

    form = OrderForm()

    template = 'checkout/checkout.html'
    
    context = {
        'form': form,
        'quote': quote,
        'stripe_public_key': stripe_public_key,
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
