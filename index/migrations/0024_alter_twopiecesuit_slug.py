# Generated by Django 3.2.7 on 2021-11-17 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0023_alter_twopiecesuit_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twopiecesuit',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]