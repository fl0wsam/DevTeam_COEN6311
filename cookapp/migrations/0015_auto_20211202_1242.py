# Generated by Django 3.0 on 2021-12-02 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookapp', '0014_auto_20211202_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]