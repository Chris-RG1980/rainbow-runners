# Generated by Django 4.2.10 on 2024-03-01 17:57

from django.db import migrations
import django_bleach.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_rename_created_posts_created_date_posts_edited_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='body',
            field=django_bleach.models.BleachField(),
        ),
    ]
