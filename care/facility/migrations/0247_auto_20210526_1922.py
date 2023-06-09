# Generated by Django 2.2.11 on 2021-05-26 13:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("facility", "0246_facilityinventorylog_probable_accident"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shiftingrequest",
            name="breathlessness_level",
            field=models.IntegerField(
                choices=[
                    (10, "NOT SPECIFIED"),
                    (15, "NOT BREATHLESS"),
                    (20, "MILD"),
                    (30, "MODERATE"),
                    (40, "SEVERE"),
                ],
                default=10,
            ),
        ),
    ]
