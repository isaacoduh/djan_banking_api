# Generated by Django 4.2.15 on 2025-02-15 21:14

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ("user_profile", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="country",
            field=django_countries.fields.CountryField(
                default="NGN", max_length=5, verbose_name="Country"
            ),
        ),
    ]
