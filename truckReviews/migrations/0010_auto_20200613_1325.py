# Generated by Django 3.0.6 on 2020-06-13 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('truckReviews', '0009_auto_20200604_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='category',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='review',
            name='quality_and_taste',
            field=models.IntegerField(choices=[(1, 'Positive'), (0, 'Neutral'), (-1, 'Negative')], default=[(1, 'Positive'), (0, 'Neutral'), (-1, 'Negative')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='speed_of_service',
            field=models.IntegerField(choices=[(1, 'Positive'), (0, 'Neutral'), (-1, 'Negative')], default=[(1, 'Positive'), (0, 'Neutral'), (-1, 'Negative')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='value_for_money',
            field=models.IntegerField(choices=[(1, 'Positive'), (0, 'Neutral'), (-1, 'Negative')], default=[(1, 'Positive'), (0, 'Neutral'), (-1, 'Negative')]),
        ),
    ]
