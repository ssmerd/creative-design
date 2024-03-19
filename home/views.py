from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .forms import QuoteForm
from .models import Quote


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
            # messages.success(request, 'Successfully added quote!')
            context = {
                'quote': quote,
            }
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

def quote_detail(request):
    """ A view to show individual quote details """

    context = {
        'quote': quote,
    }

    template = 'home/quote_detail.html'

    return render(request, template, context)