# Generated by Django 4.2.15 on 2025-02-20 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="bankaccount",
            old_name="full_activated",
            new_name="fully_activated",
        ),
    ]
