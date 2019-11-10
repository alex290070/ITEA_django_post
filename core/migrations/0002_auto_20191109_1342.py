# Generated by Django 2.2.6 on 2019-11-09 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='show',
            field=models.BooleanField(default=True, verbose_name='show?'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comment',
            field=models.TextField(verbose_name='Text of comment'),
        ),
    ]