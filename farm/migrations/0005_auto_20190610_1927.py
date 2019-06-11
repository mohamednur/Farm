# Generated by Django 2.2 on 2019-06-10 16:27

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0004_produce'),
    ]

    operations = [
        migrations.AddField(
            model_name='produce',
            name='amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='produce',
            name='crop',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='farm.Crops'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produce',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produce',
            name='emp_name',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='farm.UserProfile'),
            preserve_default=False,
        ),
    ]
