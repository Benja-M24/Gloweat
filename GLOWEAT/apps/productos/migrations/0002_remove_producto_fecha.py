# Generated by Django 2.2.1 on 2019-06-24 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='fecha',
        ),
    ]