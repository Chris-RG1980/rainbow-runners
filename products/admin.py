from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget
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


class MetadataAdminForm(forms.ModelForm):
    value = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Metadata
        fields = '__all__'


class MetadataAdmin(admin.ModelAdmin):
    form = MetadataAdminForm
    filter_horizontal = ('products',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('friendly_name', 'name')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Metadata, MetadataAdmin)
admin.site.register(MetadataCategories)
