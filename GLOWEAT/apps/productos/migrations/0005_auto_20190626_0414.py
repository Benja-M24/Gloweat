# Generated by Django 2.2.1 on 2019-06-26 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0004_categorias_id_prod'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorias',
            name='id_prod',
        ),
        migrations.AlterField(
            model_name='producto',
            name='id_categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.categorias'),
        ),
    ]
