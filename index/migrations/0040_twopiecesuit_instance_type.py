# Generated by Django 3.2.7 on 2021-12-01 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0039_alter_twopiecesuit_lining'),
    ]

    operations = [
        migrations.AddField(
            model_name='twopiecesuit',
            name='instance_type',
            field=models.CharField(default='two_piece_suit', editable=False, max_length=100),
        ),
    ]
