# Generated by Django 4.1.7 on 2023-03-07 19:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="CropSeasonModel",
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
                ("name", models.CharField(max_length=1200)),
                ("timestamp", models.DateField(auto_now_add=True)),
                ("updated", models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="FarmPlotModel",
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
                ("name", models.CharField(max_length=1200)),
                ("size", models.CharField(max_length=1200)),
                ("farm_location", models.CharField(max_length=1200)),
                ("Soil_type", models.CharField(max_length=1200)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CropModel",
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
                ("name", models.CharField(max_length=1200)),
                ("type", models.CharField(max_length=1200)),
                ("description", models.TextField()),
                ("ogc", models.TextField(verbose_name="optimum_growing_condition")),
                ("market_value", models.IntegerField()),
                (
                    "status",
                    models.CharField(
                        choices=[("A", "Active"), ("N", "Active"), ("P", "Pending")],
                        max_length=1,
                    ),
                ),
                ("timestamp", models.DateField(auto_now_add=True)),
                ("updated", models.DateField(auto_now=True)),
                (
                    "season",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="farmer.cropseasonmodel",
                    ),
                ),
            ],
        ),
    ]