# Generated by Django 3.0 on 2021-11-30 17:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookapp', '0007_rating_total_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='score',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='recipe',
            name='total_score',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
    ]
