# Generated by Django 3.2.7 on 2021-11-01 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_sidebarelements'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SideBarElements',
            new_name='SideBarElement',
        ),
    ]