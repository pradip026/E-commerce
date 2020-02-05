# Generated by Django 3.0.2 on 2020-01-15 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_blogpost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='blogdescription',
            new_name='blogdescription_para1',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='blogdescription_para2',
            field=models.TextField(blank=True, default='Description', max_length=10000),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='blogdescription_para3',
            field=models.TextField(blank=True, default='Description', max_length=10000),
        ),
    ]