# Generated by Django 4.2.3 on 2023-11-21 21:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("userauths", "0005_rename_description_transaction_transaction_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="transaction",
            name="least_amount",
            field=models.DecimalField(
                decimal_places=2, default="0.00", max_digits=1000
            ),
        ),
        migrations.AddField(
            model_name="transaction",
            name="max_amount",
            field=models.DecimalField(
                decimal_places=2, default="0.00", max_digits=1000
            ),
        ),
        migrations.AddField(
            model_name="transaction",
            name="title",
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
