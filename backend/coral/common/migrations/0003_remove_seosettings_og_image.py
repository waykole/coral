# Generated by Django 3.0.5 on 2020-04-25 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20200425_1414'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seosettings',
            name='og_image',
        ),
    ]