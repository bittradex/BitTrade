# Generated by Django 4.2.3 on 2023-12-11 16:50

from django.db import migrations
import shortuuid.django_fields


class Migration(migrations.Migration):
    dependencies = [
        ("userauths", "0015_transaction_percentage_return"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="referral_code",
            field=shortuuid.django_fields.ShortUUIDField(
                alphabet="abcdefgh12345",
                length=10,
                max_length=20,
                prefix="meta",
                unique=True,
            ),
        ),
    ]
