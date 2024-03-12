from django.db import models
import json

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

    class Meta:
        verbose_name_plural = "Categories"


class Product(models.Model):
    category = models.ForeignKey(
        'Category',
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
        max_length=254
    )
    description = models.TextField()
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )
    key_features = models.TextField(
        null=True,
        blank=True
    )
    material = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    care_instructions = models.TextField(
        null=True,
        blank=True
    )
    colour = models.TextField(
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
        return self.name

    # Helper method to serialize a list of features into a JSON string
    def set_key_features(self, key_features_json):
        self.key_features = key_features_json

    # Helper method to deserialize the features JSON string
    def get_key_features(self):
        try:
            return json.loads(self.key_features) if self.key_features else []
        except json.JSONDecodeError:
            return []

    # Helper method to serialize care instructions into a JSON string
    def set_care_instructions(self, care_instructions_json):
        self.care_instructions = care_instructions_json

    # Helper method to deserialize the care instructions JSON string
    def get_care_instructions(self):
        try:
            return json.loads(
                self.care_instructions) if self.care_instructions else []
        except json.JSONDecodeError:
            return []
