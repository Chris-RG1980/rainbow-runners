from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Category, Product, Metadata, MetadataCategories

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    """
    Admin interface for viewing and editing product details.
    """

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
    """
    Form for editing Metadata using a rich text editor.
    """

    value = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Metadata
        fields = '__all__'


class MetadataAdmin(admin.ModelAdmin):
    """
    Admin interface for Metadata with rich text editing capabilities.
    """

    form = MetadataAdminForm
    filter_horizontal = ('products',)


class CategoryAdmin(admin.ModelAdmin):
    """
    Admin interface for viewing and editing category details.
    """
    list_display = ('friendly_name', 'name')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Metadata, MetadataAdmin)
admin.site.register(MetadataCategories)
