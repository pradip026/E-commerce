# Generated by Django 3.0.2 on 2020-01-13 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20200112_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='item_alone_view',
            field=models.ImageField(default=True, upload_to='productImages'),
        ),
    ]