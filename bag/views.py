# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render, redirect, reverse, HttpResponse, \
    get_object_or_404
from django.conf import settings
from django.contrib import messages

# Internal:
from products.models import Product
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def view_bag(request):
    """ A view that renders the bag contents page """

    context = {
        'max_quantity': settings.MAX_QUANTITY_FOR_PRODUCT,
    }

    return render(request, 'bag/bag.html', context)


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if quantity > settings.MAX_QUANTITY_FOR_PRODUCT:
        messages.error(
            request,
            f'Maximum quantity allowed is {settings.MAX_QUANTITY_FOR_PRODUCT}')
        return redirect(redirect_url)

    if item_id in list(bag.keys()):
        if bag[item_id]+quantity > settings.MAX_QUANTITY_FOR_PRODUCT:
            messages.error(
                request,
                f'You have reached the maximum quantity allowed: '
                f'{settings.MAX_QUANTITY_FOR_PRODUCT}')
            return redirect(redirect_url)
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})
    if quantity > 0:
        if quantity <= 15:
            bag[item_id] = quantity
            messages.success(request, f'Quantity updated')
        else:
            messages.error(
                request,
                f'Maximum quantity allowed is '
                f'{settings.MAX_QUANTITY_FOR_PRODUCT}')
    else:
        bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        bag = request.session.get('bag', {})
        bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
