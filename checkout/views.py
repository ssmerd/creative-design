from django.shortcuts import render

def checkout(request):
    """
        A view to return the index page
    """


    template = 'checkout/checkout_details.html'
    
    context = {
        'quote': request.session['quote'],
    }

    return render(request, template, context)
