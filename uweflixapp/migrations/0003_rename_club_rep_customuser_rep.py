# Generated by Django 4.0.4 on 2022-05-09 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uweflixapp', '0002_customuser_active_customuser_club_rep_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='club_rep',
            new_name='rep',
        ),
    ]
