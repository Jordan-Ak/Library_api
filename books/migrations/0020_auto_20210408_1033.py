# Generated by Django 3.1.7 on 2021-04-08 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0019_auto_20210408_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quantity',
            name='book',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='books.book'),
        ),
    ]
