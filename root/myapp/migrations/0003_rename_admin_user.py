# Generated by Django 4.0.5 on 2022-06-11 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_user_admin'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Admin',
            new_name='USER',
        ),
    ]
