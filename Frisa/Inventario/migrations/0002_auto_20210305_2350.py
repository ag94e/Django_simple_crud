# Generated by Django 3.1.7 on 2021-03-05 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modeloinventario',
            name='cantidad',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='modeloinventario',
            name='codigo',
            field=models.IntegerField(),
        ),
    ]
