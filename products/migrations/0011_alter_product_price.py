# Generated by Django 4.1 on 2024-04-15 18:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_alter_metadata_category_alter_metadata_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]