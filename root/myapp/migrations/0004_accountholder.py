# Generated by Django 4.0.5 on 2022-06-11 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_rename_admin_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='accountholder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
