# Generated by Django 5.0 on 2023-12-25 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myBankApp', '0008_alter_cliente_dni_alter_cliente_telefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='dni',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.IntegerField(),
        ),
    ]
