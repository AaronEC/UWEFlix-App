# Generated by Django 4.0.3 on 2022-05-04 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uweflixapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='adult_ticket',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='child_ticket',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='student_ticket',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='description',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='universityclub',
            name='debit_amount',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
