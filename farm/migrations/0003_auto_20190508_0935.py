# Generated by Django 2.2 on 2019-05-08 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0002_crops'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crops',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
