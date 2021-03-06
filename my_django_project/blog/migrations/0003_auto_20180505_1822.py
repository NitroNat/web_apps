# Generated by Django 2.0.5 on 2018-05-05 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180505_1632'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='publication_date',
            new_name='pub_date',
        ),
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(blank=True, max_length=254, unique=True),
        ),
    ]
