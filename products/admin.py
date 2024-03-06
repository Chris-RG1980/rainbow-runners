from django.contrib import admin
from .models import Category, Product

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('sku',
                    'name',
                    'category',
                    'price',
                    'key_features',
                    'material',
                    'care_instructions',
                    'colour',
                    'image'
                    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('friendly_name', 'name')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
