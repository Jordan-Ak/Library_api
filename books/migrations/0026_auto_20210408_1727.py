# Generated by Django 3.1.7 on 2021-04-08 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0025_auto_20210408_1707'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quantity_borrowed',
            options={'verbose_name_plural': 'Quantity_Borrowed'},
        ),
    ]
