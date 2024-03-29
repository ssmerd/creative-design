from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .forms import QuoteForm


def index(request):
    """
        A view to return the index page
    """

    form = QuoteForm()

    template = 'home/index.html'
    
    context = {
        'form': form,
    }

    return render(request, template, context)

def add_quote(request):

    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote = form.cleaned_data
            price = calculate_price(quote)
    
            context = {
                'category': quote['category'].name,
                'name': quote['name'],
                'description': quote['description'],
                'size': quote['size'],
                'price': price
            }

            request.session['quote'] = context

            messages.success(request, "You have added a quote")
            return render(request, "home/quote_detail.html", context)
        else:
            messages.error(request,
                           ('Failed to add quote. '
                            'Please ensure the form is valid.'))
    else:
        form = QuoteForm()

    template = 'home/index.html'
    
    context = {
        'form': form,
    }

    return render(request, template, context)

def calculate_price(quote):
    category = quote['category']

    total_price = 0

    if category.name.upper() == "graphics".upper():
        total_price = total_price + 100
    elif category.name.upper() == "illustrations".upper():
        total_price = total_price +  120
    elif category.name.upper() == "icon".upper():
        total_price = total_price +  70
    elif category.name.upper() == "graphics".upper():
        total_price = total_price +  150

    return total_price
