# Generated by Django 5.1.2 on 2024-10-18 14:02

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="note",
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
                ("nName", models.CharField(max_length=30)),
                ("nDate", models.DateField()),
                ("nDescription", models.TextField(null=True)),
            ],
        ),
    ]
