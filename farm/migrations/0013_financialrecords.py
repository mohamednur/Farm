# Generated by Django 2.2 on 2019-06-18 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0012_auto_20190613_1904'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinancialRecords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipt_no', models.CharField(max_length=30)),
                ('Amount', models.FloatField()),
                ('date_of_payment', models.DateTimeField()),
            ],
        ),
    ]
