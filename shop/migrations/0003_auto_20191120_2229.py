# Generated by Django 2.2.7 on 2019-11-20 15:29

from django.db import migrations, models
import shop.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20191119_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to=shop.models.get_file_path),
        ),
    ]
