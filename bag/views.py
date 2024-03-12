from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from products.models import Product

# Create your views here.


def view_bag(request):
    """ A view to return the shopping bag page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
                msg = (f'Updated size {size.upper()} '
                       f'{product.name} quantity to '
                       f'{bag[item_id]["items_by_size"][size]}')
                messages.success(request, msg)
            else:
                bag[item_id]['items_by_size'][size] = quantity
                msg = (f'Added size {size.upper()} '
                       f'{product.name} to your bag')
                messages.success(request, msg)
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
            msg = (f'Added size {size.upper()} {product.name} to your bag')
            messages.success(request, msg)
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            msg = (f'Updated {product.name} quantity to {bag[item_id]}')
            messages.success(request, msg)
        else:
            bag[item_id] = quantity
            msg = (f'Added {product.name} to your bag')
            messages.success(request, msg)

    request.session['bag'] = bag
    return redirect(redirect_url)
