# Generated by Django 2.0.5 on 2018-05-05 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180505_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Author Name'),
        ),
    ]
