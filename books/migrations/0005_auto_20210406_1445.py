# Generated by Django 3.1.7 on 2021-04-06 13:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0004_remove_book_ratings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.IntegerField(),
        ),
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together={('who_rated', 'book_rated')},
        ),
    ]
