# Generated by Django 3.2.9 on 2022-02-22 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_alter_product_pimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pImage',
            field=models.ImageField(upload_to='image/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pNew',
            field=models.BooleanField(default=False),
        ),
    ]
