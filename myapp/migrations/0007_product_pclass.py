# Generated by Django 3.2.9 on 2022-02-22 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pClass',
            field=models.CharField(default='', max_length=20),
        ),
    ]