# Generated by Django 3.1.7 on 2021-04-06 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_remove_borrowed_has_returned'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrowed',
            name='has_returned',
            field=models.BooleanField(default=False),
        ),
    ]