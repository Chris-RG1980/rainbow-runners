from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.


class Category(models.Model):
    """
    Represents a category for products.
    """
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

    class Meta:
        verbose_name_plural = "Categories"


class Product(models.Model):
    """
    Defines the structure for a product listing in the database.
    """
    category = models.ForeignKey(
        Category,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    sku = models.CharField(
        max_length=254,
        null=True,
        blank=True
    )
    name = models.CharField(
        max_length=254,
        null=False,
        blank=False,
    )
    description = models.TextField(
        null=False,
        blank=False,
    )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )

    material = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    colour = models.CharField(
        max_length=30,
        null=True,
        blank=True
    )
    image = models.ImageField(
        null=True,
        blank=True
    )
    has_sizes = models.BooleanField(
        default=False,
        null=True,
        blank=True
    )

    def __str__(self):
        return f'[{self.id}] {self.name}'

    def get_key_features(self):
        """
        Returns product's key features.
        """
        return Metadata.objects.filter(products__id=self.id,
                                       category__name='key_features')

    def get_care_instructions(self):
        """
        Returns product's care instructions.
        """
        return Metadata.objects.filter(products__id=self.id,
                                       category__name='care_instructions')

    def get_size_guide(self):
        """
        Returns product's size guide.
        """
        return Metadata.objects.filter(products__id=self.id,
                                       category__name='size_guide')

    def get_sizes(self):
        """
        Returns product's available sizes.
        """
        return Metadata.objects.filter(products__id=self.id,
                                       category__name='sizes')


class MetadataCategories(models.Model):
    """
    Category for classifying product metadata.
    """
    def __str__(self):
        return self.name

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def get_friendly_name(self):
        return self.friendly_name

    class Meta:
        verbose_name_plural = "Metadata Categories"
        db_table = "products_metadata_categories"


class Metadata(models.Model):
    """
    Metadata entries linked to products, classified under categories.
    """
    def __str__(self):
        return f'[{self.id}] {self.category}'

    products = models.ManyToManyField(
        Product,
        blank=True,
        related_name="Metadata",
    )

    category = models.ForeignKey(
        MetadataCategories,
        null=False,
        blank=False,
        on_delete=models.RESTRICT
    )

    value = models.TextField(
        null=False,
        blank=False,
        verbose_name="Input Product Information"
    )

    def get_sizes():
        """
        Filter and return sizes from metadata.
        """
        return Metadata.objects.filter(category__name='sizes')

    class Meta:
        verbose_name_plural = "metadata"
