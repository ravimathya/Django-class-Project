# Generated by Django 2.2.1 on 2019-05-08 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Story',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]