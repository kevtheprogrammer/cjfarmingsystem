# Generated by Django 4.1.7 on 2023-03-14 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("farmer", "0006_remove_croprotationmodel_crop_croprotationmodel_crop"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cropmodel",
            name="status",
            field=models.CharField(
                choices=[("A", "Active"), ("P", "Pending"), ("I", "Inactive")],
                max_length=1,
            ),
        ),
        migrations.CreateModel(
            name="ReportModel",
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
                ("title", models.CharField(max_length=50)),
                ("discription", models.TextField()),
                ("timestamp", models.DateField(auto_now_add=True)),
                ("updated", models.DateField(auto_now=True)),
                (
                    "item",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="farmer.croprotationmodel",
                    ),
                ),
            ],
        ),
    ]