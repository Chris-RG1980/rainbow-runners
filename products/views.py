from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models.functions import Lower
from django.contrib import messages
from django.urls import reverse
from django.views.decorators.http import require_POST
from .models import Product, Metadata, MetadataCategories
from .forms import ProductForm, MetadataForm

# Create your views here.


def all_products(request):
    """A view to show all products, including sorting and search queries"""

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
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product
    }

    return render(request, 'products/product_detail.html', context)


def add_product(request):
    """A view to add a product"""

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


def add_product_info(request, product_id):
    """A view to select the metadata to add"""

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


def add_product_metadata(request, product_id, metadata_category_id):
    """A view to add metadata"""

    product = get_object_or_404(Product, pk=product_id)
    metadata_category = get_object_or_404(
        MetadataCategories,
        pk=metadata_category_id
    )

    if metadata_category.name == 'sizes':
        msg = "Please select a size or add a new size"
        messages.error(request, msg)
        return redirect(reverse(
                'add_product_info',
                kwargs={'product_id': product_id})
            )

    if request.method == "POST":
        form = MetadataForm(request.POST)
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

    else:
        form = MetadataForm()

    context = {
                'product': product,
                'metadata_category': metadata_category,
                'form': form,
            }

    return render(request, 'products/add_metadata.html', context)


@require_POST
def process_metadata_size(request, product_id):

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
