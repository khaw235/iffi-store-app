# Generated by Django 3.2.7 on 2021-11-01 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_alter_shirtmodel_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='SideBarElements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('img', models.FileField(null=True, upload_to='sidebar-elements/', verbose_name='Picture')),
            ],
        ),
    ]
