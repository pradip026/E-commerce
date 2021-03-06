# Generated by Django 3.0.2 on 2020-01-20 07:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_auto_20200119_2008'),
    ]

    operations = [
        migrations.CreateModel(
            name='productreview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('useremail', models.EmailField(max_length=254)),
                ('reviewsms', models.CharField(max_length=1000)),
                ('productid', models.IntegerField()),
                ('productstar', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 1, 20, 13, 15, 40, 220151)),
        ),
    ]
