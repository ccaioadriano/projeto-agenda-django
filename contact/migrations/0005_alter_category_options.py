# Generated by Django 5.0 on 2024-01-03 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_category_contact_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
    ]