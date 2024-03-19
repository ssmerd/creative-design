from django.shortcuts import render, redirect, reverse, get_list_or_404
from .models import Design, Category
from django.contrib import messages
from django.conf import settings
from django.db.models import Q



def all_designs(request):
    """
        A view to show all designs
    """

    designs = Design.objects.all()
    query = None
    categories = None

    if request.GET:

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            designs = designs.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria")
                return redirect(reverse('designs'))
            queries = Q(name__contains=query) | Q(description__icontains=query)
            designs = designs.filter(queries)
           


    context = {
        'designs': designs,
        'MEDIA_URL': settings.MEDIA_URL,
        'search_term': query,
    }

    return render(request ,"designs/designs.html", context)