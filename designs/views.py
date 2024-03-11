from django.shortcuts import render
from .models import Design
from django.conf import settings

def all_designs(request):
    """
        A view to show all designs
    """

    designs = Design.objects.all()

    context = {
        'designs': designs,
        'MEDIA_URL': settings.MEDIA_URL
    }

    return render(request ,"designs/designs.html", context)