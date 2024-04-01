from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path(
        'add_info/<int:product_id>/',
        views.add_product_info,
        name='add_product_info'),
    path(
        '<int:product_id>/metadata/<int:metadata_category_id>',
        views.add_product_metadata,
        name='add_product_metadata'),
    path(
        '<int:product_id>/metadata/size',
        views.process_metadata_size,
        name='process_metadata_size'),
]
