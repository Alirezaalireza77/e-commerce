# Generated by Django 5.1.1 on 2024-09-16 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_category_parent_alter_order_name_alter_order_product_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='parent',
        ),
    ]