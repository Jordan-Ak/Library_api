# Generated by Django 3.1.7 on 2021-04-06 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0016_auto_20210406_2029'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Quantities',
            new_name='Quantity',
        ),
        migrations.AlterModelOptions(
            name='quantity',
            options={'verbose_name_plural': 'Quantities'},
        ),
    ]
