from django.contrib import admin
from .models import Category, Product, Metadata, MetadataCategories

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('sku',
                    'name',
                    'category',
                    'price',
                    'material',
                    'colour',
                    'image',
                    'has_sizes'
                    )


class MetadataAdmin(admin.ModelAdmin):
    filter_horizontal = ('products',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('friendly_name', 'name')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Metadata, MetadataAdmin)
admin.site.register(MetadataCategories)
