# Generated by Django 5.0.6 on 2024-05-24 15:56

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_emailcampaign"),
    ]

    operations = [
        migrations.AlterField(
            model_name="emailcampaign",
            name="message",
            field=ckeditor.fields.RichTextField(),
        ),
    ]
