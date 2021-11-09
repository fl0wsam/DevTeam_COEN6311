# Generated by Django 3.0 on 2021-11-08 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cookapp', '0002_auto_20211108_1218'),
    ]

    operations = [
        migrations.AddField(
            model_name='rate',
            name='recipe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cookapp.Recipe'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='cook_duration',
            field=models.IntegerField(default=0),
        ),
    ]
