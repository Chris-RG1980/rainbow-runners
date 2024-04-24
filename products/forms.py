from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Metadata


class ProductForm(forms.ModelForm):
    """
    Form for creating and updating Product instances.
    """

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(
        label='Image',
        required=False,
        widget=CustomClearableFileInput
    )

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['description'].label = "Description"
        self.auto_id = 'product_%s'
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class MetadataForm(forms.ModelForm):
    """
    Form for adding or editing metadata related to products.
    """

    class Meta:
        model = Metadata
        fields = ('value',)

    def __init__(self, *args, **kwargs):
        super(MetadataForm, self).__init__(*args, **kwargs)
        self.fields['value'].label = "Add product information here"
        self.auto_id = 'metadata_%s'
