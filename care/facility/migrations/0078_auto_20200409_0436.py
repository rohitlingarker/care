# Generated by Django 2.2.11 on 2020-04-08 23:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("facility", "0077_auto_20200409_0422"),
    ]

    operations = [
        migrations.AddField(
            model_name="historicalpatientregistration",
            name="aadhar_no",
            field=models.CharField(
                default="", max_length=255, verbose_name="Aadhar Number of Patient"
            ),
        ),
        migrations.AddField(
            model_name="historicalpatientregistration",
            name="nationality",
            field=models.CharField(
                default="", max_length=255, verbose_name="Nationality of Patient"
            ),
        ),
        migrations.AddField(
            model_name="historicalpatientregistration",
            name="passport_no",
            field=models.CharField(
                default="",
                max_length=255,
                verbose_name="Passport Number of Foreign Patients",
            ),
        ),
        migrations.AddField(
            model_name="patientregistration",
            name="aadhar_no",
            field=models.CharField(
                default="", max_length=255, verbose_name="Aadhar Number of Patient"
            ),
        ),
        migrations.AddField(
            model_name="patientregistration",
            name="nationality",
            field=models.CharField(
                default="", max_length=255, verbose_name="Nationality of Patient"
            ),
        ),
        migrations.AddField(
            model_name="patientregistration",
            name="passport_no",
            field=models.CharField(
                default="",
                max_length=255,
                verbose_name="Passport Number of Foreign Patients",
            ),
        ),
    ]
