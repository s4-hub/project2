# Generated by Django 2.2.7 on 2019-11-19 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.IntegerField(blank=True, choices=[(1, 'SMALL'), (2, 'MEDIUM'), (3, 'LARGE'), (4, 'EXTRA LARGE')], null=True),
        ),
    ]