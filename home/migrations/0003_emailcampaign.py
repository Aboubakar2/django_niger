# Generated by Django 5.0.6 on 2024-05-24 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_subscriber_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="EmailCampaign",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("subject", models.CharField(max_length=255)),
                ("message", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]