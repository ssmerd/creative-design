from django.shortcuts import render

def view_bag(request):
    """
        A view to see the content of a bag
    """

    template = 'bag/bag.html'

    return render(request, template)

