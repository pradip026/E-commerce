# Generated by Django 3.0.2 on 2020-01-15 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20200115_0915'),
    ]

    operations = [
        migrations.CreateModel(
            name='blogpost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blogheading', models.TextField(default="Today's Heading", max_length=100)),
                ('blogtheme', models.TextField(default="Today's Heading theme", max_length=200)),
                ('blogdescription', models.TextField(default='Description', max_length=10000)),
                ('blogtags', models.CharField(default='Story', max_length=100)),
                ('blogimage', models.ImageField(upload_to='blogimage')),
            ],
        ),
    ]