# Generated by Django 4.0.4 on 2022-05-09 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uweflixapp', '0006_alter_customuser_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='showing',
            name='COVID_toggle',
            field=models.BooleanField(default=False),
        ),
    ]
