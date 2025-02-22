# Generated by Django 4.2.15 on 2025-02-22 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_rename_full_activated_bankaccount_fully_activated"),
    ]

    operations = [
        migrations.AddField(
            model_name="bankaccount",
            name="interest_rate",
            field=models.DecimalField(
                decimal_places=4,
                default=0.0,
                help_text="Annual Interest rate as a decimal (e.g 0.0150 for 1.5%)",
                max_digits=5,
                verbose_name="Interest Rate",
            ),
        ),
        migrations.AlterField(
            model_name="bankaccount",
            name="fully_activated",
            field=models.BooleanField(default=False, verbose_name="Fully Activated"),
        ),
        migrations.AlterField(
            model_name="transaction",
            name="transaction_type",
            field=models.CharField(
                choices=[
                    ("deposit", "Deposit"),
                    ("withdrawal", "Withdrawal"),
                    ("transfer", "Transfer"),
                    ("interest", "Interest"),
                ],
                max_length=20,
            ),
        ),
    ]
