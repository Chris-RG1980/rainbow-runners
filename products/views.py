from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models.functions import Lower
from django.contrib import messages
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from .models import Product, Metadata, MetadataCategories
from .forms import ProductForm, MetadataForm

# Create your views here.


def is_in_group(user, group_name):
    """Check if the user is in the given group."""
    return user.groups.filter(name=group_name).exists()


def all_products(request):
    """A view to show all products, including sorting and search queries"""

    is_admin = is_in_group(request.user, 'admin')

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if 'sort' in request.GET:
        sortkey = request.GET['sort']
        sort = sortkey
        if sortkey == 'name':
            sortkey = 'lower_name'
            products = products.annotate(lower_name=Lower('name'))

        if 'direction' in request.GET:
            direction = request.GET['direction']
            if direction == 'desc':
                sortkey = f'-{sortkey}'
        products = products.order_by(sortkey)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'is_admin': is_admin
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """A view to add a product"""

    is_admin = is_in_group(request.user, 'admin')

    if not is_admin:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect('products')

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid() and request.user.is_authenticated:
            new_product = form.save()
            msg = "Product saved, add further info as required"
            messages.success(request, msg)
            return redirect(reverse(
                'add_product_info',
                kwargs={'product_id': new_product.pk})
            )
        else:
            msg = "Failed to save product. Please ensure the form is valid."
            messages.error(request, msg)
    else:
        form = ProductForm()
    context = {
        'form': form,
    }
    return render(request, 'products/add_products.html', context)


@login_required
def add_product_info(request, product_id):
    """A view to select the metadata to add"""

    is_admin = is_in_group(request.user, 'admin')

    if not is_admin:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect('products')

    product = get_object_or_404(Product, pk=product_id)
    sizes = Metadata.get_sizes()
    metadata_categories = MetadataCategories.objects.exclude(name='sizes')

    for size in sizes:
        size.product_exists = size.products.filter(pk=product_id).exists()

    context = {
            'product': product,
            'sizes': sizes,
            'metadata_categories': metadata_categories,
        }
    return render(request, 'products/add_product_info.html', context)


@login_required
def add_product_metadata(request, product_id, metadata_category_id):
    """A view to add metadata"""

    is_admin = is_in_group(request.user, 'admin')

    if not is_admin:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect('products')

    product = get_object_or_404(Product, pk=product_id)
    metadata_category = get_object_or_404(
        MetadataCategories,
        pk=metadata_category_id
    )

    product_metadata = Metadata.objects.filter(
        products__id=product_id).filter(
            category__id=metadata_category_id).first()

    form = MetadataForm()

    if product_metadata is not None:
        form.initial['value'] = product_metadata.value

    if metadata_category.name == 'sizes':
        msg = "Please select a size or add a new size"
        messages.error(request, msg)
        return redirect(reverse(
                'add_product_info',
                kwargs={'product_id': product_id})
            )

    if request.method == "POST":
        form = MetadataForm(request.POST, instance=product_metadata)
        if form.is_valid() and request.user.is_authenticated:
            metadata = form.save(commit=False)
            metadata.category = metadata_category
            metadata.save()
            metadata.products.add(product)
            metadata.save()
            msg = (
                "Product Information saved."
                " Add more product information if required"
            )
            messages.success(request, msg)
            return redirect(reverse(
                'add_product_info',
                kwargs={'product_id': product_id})
            )
        else:
            msg = (
                "Failed to add product information."
                " Please ensure the form is valid."
            )
            messages.error(request, msg)

    context = {
                'product': product,
                'metadata_category': metadata_category,
                'form': form,
            }

    return render(request, 'products/add_metadata.html', context)


@login_required
@require_POST
def process_metadata_size(request, product_id):
    """A view to add and remove sizes"""

    is_admin = is_in_group(request.user, 'admin')

    if not is_admin:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect('products')

    product = get_object_or_404(Product, pk=product_id)
    metadata_size_id = request.POST.get("size-id")
    action = request.POST.get("action")

    if metadata_size_id is None:
        return HttpResponse(status=404)

    metadata = get_object_or_404(
        Metadata,
        pk=metadata_size_id
    )

    if metadata.category.name != "sizes":
        return HttpResponse(status=404)

    if action == "add":
        metadata.products.add(product)
    else:
        metadata.products.remove(product)

    return HttpResponse(status=204)


@login_required
def edit_product(request, product_id):
    """A view to edit products"""

    is_admin = is_in_group(request.user, 'admin')

    if not is_admin:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect('products')

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully updated {product.name}!')
            return redirect('product_detail', product_id=product.id)
        else:
            msg = 'Failed to update product. Please ensure the form is valid.'
            messages.error(request, msg)
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    context = {
        'form': form,
        'product': product,
    }
    return render(request, 'products/edit_product.html', context)


@login_required
def delete_product(request, product_id):
    """A view to delete products"""

    is_admin = is_in_group(request.user, 'admin')

    if not is_admin:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect('products')

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted successfully!')
    return redirect(reverse('products'))
