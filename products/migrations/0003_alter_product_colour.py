# Generated by Django 4.2.10 on 2024-03-09 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_category_options_remove_product_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='colour',
            field=models.TextField(blank=True, null=True),
        ),
    ]
