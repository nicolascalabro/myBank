# Generated by Django 5.0 on 2023-12-25 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myBankApp', '0007_alter_cliente_dni'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='dni',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.BigIntegerField(),
        ),
    ]
