# Generated by Django 3.0.6 on 2020-05-27 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('truckReviews', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='foodtrucks',
            old_name='coverPhotoAlt',
            new_name='coverPhotoALT',
        ),
    ]