# Generated by Django 3.2.9 on 2022-02-22 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_product_pnew'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pQty',
            field=models.BooleanField(default=False),
        ),
    ]