# Generated by Django 4.0.3 on 2022-05-04 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uweflixapp', '0002_alter_booking_adult_ticket_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='showing',
            name='film',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='uweflixapp.film'),
        ),
    ]
