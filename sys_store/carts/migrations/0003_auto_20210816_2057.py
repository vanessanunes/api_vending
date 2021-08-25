# Generated by Django 3.2.6 on 2021-08-16 23:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sellers', '0001_initial'),
        ('clients', '0001_initial'),
        ('carts', '0002_auto_20210815_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.client'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='seller',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sellers.seller'),
        ),
    ]