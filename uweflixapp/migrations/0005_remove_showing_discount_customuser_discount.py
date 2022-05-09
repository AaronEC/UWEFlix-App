# Generated by Django 4.0.4 on 2022-05-09 18:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uweflixapp', '0004_remove_customuser_club_showing_discount_delete_club'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='showing',
            name='discount',
        ),
        migrations.AddField(
            model_name='customuser',
            name='discount',
            field=models.IntegerField(default=10, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
    ]