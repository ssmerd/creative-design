from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Design, Category
from .forms import DesignForm



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
                return redirect(reverse('home'))
            queries = Q(name__contains=query) | Q(description__icontains=query)
            designs = designs.filter(queries)

    context = {
        'designs': designs,
        'search_term': query,
    }

    return render(request ,"designs/designs.html", context)


@login_required
def add_design(request):
    """ Add a design to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = DesignForm(request.POST, request.FILES)
        if form.is_valid():
            design = form.save()
            messages.success(request, 'Successfully added design!')
            return redirect(reverse('designs'))
        else:
            messages.error(request,
                           ('Failed to add design. '
                            'Please ensure the form is valid.'))
    else:
        form = DesignForm()

    template = 'designs/add_design.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_design(request, design_id):
    """ Edit a design"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    design = get_object_or_404(Design, pk=design_id)
    if request.method == 'POST':
        form = DesignForm(request.POST, request.FILES, instance=design)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated design!')
            return redirect(reverse('designs'))
        else:
            messages.error(request,
                           ('Failed to update design. '
                            'Please ensure the form is valid.'))
    else:
        form = DesignForm(instance=design)
        messages.info(request, f'You are editing {design.name}')

    template = 'designs/edit_design.html'
    context = {
        'form': form,
        'design': design,
    }

    return render(request, template, context)