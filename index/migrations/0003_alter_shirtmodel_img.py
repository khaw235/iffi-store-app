# Generated by Django 3.2.7 on 2021-11-01 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20211101_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shirtmodel',
            name='img',
            field=models.FileField(null=True, upload_to='', verbose_name='Picture'),
        ),
    ]