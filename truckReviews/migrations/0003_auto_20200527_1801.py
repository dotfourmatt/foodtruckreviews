# Generated by Django 3.0.6 on 2020-05-27 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('truckReviews', '0002_auto_20200527_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodtrucks',
            name='facebook',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='foodtrucks',
            name='instagram',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='foodtrucks',
            name='twitter',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='foodtrucks',
            name='website',
            field=models.TextField(default=''),
        ),
    ]
