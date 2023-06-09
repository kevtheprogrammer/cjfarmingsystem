# Generated by Django 4.1.7 on 2023-03-15 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("farmer", "0007_alter_cropmodel_status_reportmodel"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="reportmodel",
            options={"ordering": ["updated"]},
        ),
        migrations.AddField(
            model_name="cropmodel",
            name="link",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="cropmodel",
            name="upload",
            field=models.FileField(
                blank=True, max_length=1000, null=True, upload_to="upload/crop/"
            ),
        ),
    ]
