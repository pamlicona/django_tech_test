# Generated by Django 2.0.4 on 2018-10-19 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0007_auto_20181019_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locationmodel',
            name='id',
            field=models.CharField(default='loc_2018101919559dfee41dd', max_length=30, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='stationmodel',
            name='id',
            field=models.CharField(default='sta_201810191955925c4cc73', max_length=30, primary_key=True, serialize=False, unique=True),
        ),
    ]