# Generated by Django 3.0.2 on 2020-01-18 13:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_auto_20200118_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='webabout',
            name='thought_by',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 1, 18, 19, 27, 41, 654919)),
        ),
    ]