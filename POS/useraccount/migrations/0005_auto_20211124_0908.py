# Generated by Django 3.2 on 2021-11-24 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0004_auto_20211018_0500'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bkuser',
            old_name='facebook',
            new_name='position',
        ),
        migrations.RenameField(
            model_name='bkuser',
            old_name='phoneNo_2',
            new_name='shop',
        ),
        migrations.RemoveField(
            model_name='bkuser',
            name='bio',
        ),
    ]