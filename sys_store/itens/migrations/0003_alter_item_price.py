# Generated by Django 3.2.6 on 2021-08-18 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itens', '0002_alter_item_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
    ]
