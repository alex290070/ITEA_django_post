# Generated by Django 2.2.2 on 2019-11-28 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='login',
            new_name='name',
        ),
    ]