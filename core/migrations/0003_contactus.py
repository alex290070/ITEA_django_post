# Generated by Django 2.2.2 on 2019-12-03 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField(null=True)),
                ('comment', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Обратная связь',
            },
        ),
    ]
