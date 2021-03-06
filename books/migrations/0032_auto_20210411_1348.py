# Generated by Django 3.1.7 on 2021-04-11 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0031_auto_20210409_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(blank=True, default='2', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='books.publisher'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
