# Generated by Django 5.0 on 2023-12-25 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myBankApp', '0003_remove_cliente_dni_remove_cliente_telefono'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='dni',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='telefono',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]