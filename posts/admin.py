from django.contrib import admin
from .models import Posts

# Register your models here.


admin.site.register(Posts)


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
