# Generated by Django 3.2.6 on 2021-08-17 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0004_alter_cart_itens'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='commission',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='total_value',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
    ]
