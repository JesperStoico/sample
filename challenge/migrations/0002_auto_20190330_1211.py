# Generated by Django 2.1.7 on 2019-03-30 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
        migrations.AlterField(
            model_name='product',
            name='price_old',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]
