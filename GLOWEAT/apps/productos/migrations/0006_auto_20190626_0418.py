# Generated by Django 2.2.1 on 2019-06-26 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0005_auto_20190626_0414'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='id_categoria',
            new_name='id_cate',
        ),
    ]