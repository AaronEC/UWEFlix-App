# Generated by Django 4.0.3 on 2022-05-08 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uweflixapp', '0002_user_rep_id_user_student_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
