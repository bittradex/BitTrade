# Generated by Django 4.2.3 on 2023-12-02 00:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("userauths", "0012_alter_transaction_amount"),
    ]

    operations = [
        migrations.AddField(
            model_name="deposit",
            name="currency",
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name="deposit",
            name="wallet_address",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
