# Generated by Django 3.1.7 on 2021-03-05 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0003_auto_20210305_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modeloinventario',
            name='ubicacion',
            field=models.CharField(max_length=13),
        ),
    ]