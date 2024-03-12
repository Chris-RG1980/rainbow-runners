from django.contrib import admin
from .models import Category, Product
from .forms import ProductAdminForm
import json

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
                    'image',
                    'has_sizes'
                    )

    form = ProductAdminForm

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        # If existing object, convert JSON back to a comma-separated list
        if obj:
            if obj.key_features:
                try:
                    key_features_list = json.loads(obj.key_features)
                    form.base_fields[
                        'key_features'
                    ].initial = ', '.join(
                        key_features_list
                    )
                except json.JSONDecodeError:
                    form.base_fields['key_features'].initial = ""

        if obj:
            if obj.care_instructions:
                try:
                    care_instructions_list = json.loads(obj.care_instructions)
                    form.base_fields[
                        'care_instructions'
                    ].initial = ', '.join(
                        care_instructions_list)
                except json.JSONDecodeError:
                    form.base_fields['care_instructions'].initial = ""

        return form


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('friendly_name', 'name')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
