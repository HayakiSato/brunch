# Generated by Django 3.2.9 on 2022-02-22 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_product_pclass'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pNew',
            field=models.BooleanField(default=True),
        ),
    ]
