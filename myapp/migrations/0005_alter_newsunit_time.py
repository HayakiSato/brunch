# Generated by Django 3.2.9 on 2022-02-21 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_newsunit_press'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsunit',
            name='time',
            field=models.DateTimeField(),
        ),
    ]
