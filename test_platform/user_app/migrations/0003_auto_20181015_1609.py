# Generated by Django 2.1.1 on 2018-10-15 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0002_auto_20181011_1817'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='module',
            name='project',
        ),
        migrations.DeleteModel(
            name='Module',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
