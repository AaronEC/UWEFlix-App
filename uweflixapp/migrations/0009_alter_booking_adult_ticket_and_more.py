# Generated by Django 4.0.3 on 2022-05-09 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uweflixapp', '0008_alter_booking_adult_ticket_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='adult_ticket',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='booking',
            name='child_ticket',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='booking',
            name='student_ticket',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
