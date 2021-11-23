# Generated by Django 3.2.7 on 2021-11-15 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0016_auto_20211115_2336'),
    ]

    operations = [
        migrations.CreateModel(
            name='Button',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('img', models.FileField(null=True, upload_to='buttons/', verbose_name='Picture')),
            ],
        ),
        migrations.CreateModel(
            name='ButtonHoleThread',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('img', models.FileField(null=True, upload_to='button-hole-threads/', verbose_name='Picture')),
            ],
        ),
        migrations.CreateModel(
            name='Contrast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('img', models.FileField(null=True, upload_to='contrasts/', verbose_name='Picture')),
            ],
        ),
        migrations.CreateModel(
            name='Fabric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('img', models.FileField(null=True, upload_to='fabrics/', verbose_name='Picture')),
            ],
        ),
        migrations.CreateModel(
            name='Lapel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('img', models.FileField(null=True, upload_to='lapels/', verbose_name='Picture')),
            ],
        ),
        migrations.CreateModel(
            name='Lining',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('img', models.FileField(null=True, upload_to='linings/', verbose_name='Picture')),
            ],
        ),
        migrations.CreateModel(
            name='Pocket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('img', models.FileField(null=True, upload_to='pockets/', verbose_name='Picture')),
            ],
        ),
        migrations.CreateModel(
            name='TrouserBackPocket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('img', models.FileField(null=True, upload_to='trouser-back-pockets/', verbose_name='Picture')),
            ],
        ),
        migrations.CreateModel(
            name='TrouserButtoning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('img', models.FileField(null=True, upload_to='trouser-buttonings/', verbose_name='Picture')),
            ],
        ),
        migrations.CreateModel(
            name='TrouserPocket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('img', models.FileField(null=True, upload_to='trouser-pockets/', verbose_name='Picture')),
            ],
        ),
        migrations.CreateModel(
            name='TrouserTurnUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('img', models.FileField(null=True, upload_to='trouser-turn-ups/', verbose_name='Picture')),
            ],
        ),
        migrations.CreateModel(
            name='Vent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('img', models.FileField(null=True, upload_to='vents/', verbose_name='Picture')),
            ],
        ),
        migrations.AlterField(
            model_name='buttoning',
            name='img',
            field=models.FileField(null=True, upload_to='buttonings/', verbose_name='Picture'),
        ),
    ]