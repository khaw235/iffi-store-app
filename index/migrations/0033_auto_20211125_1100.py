# Generated by Django 3.2.7 on 2021-11-25 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0032_auto_20211124_2207'),
    ]

    operations = [
        migrations.AddField(
            model_name='twopiecesuit',
            name='counts',
            field=models.IntegerField(default=0, editable=False, max_length=10),
        ),
        migrations.AlterField(
            model_name='twopiecesuit',
            name='vent',
            field=models.CharField(choices=[('single vent', 'Single vent'), ('double vent', 'Double vent')], max_length=100, null=True),
        ),
    ]
