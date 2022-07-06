# Generated by Django 3.2.13 on 2022-07-04 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("edc_qol", "0002_historicalsf12_sf12"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="historicaleq5d3l",
            options={
                "get_latest_by": ("history_date", "history_id"),
                "ordering": ("-history_date", "-history_id"),
                "verbose_name": "historical EuroQol EQ-5D-3L Instrument",
                "verbose_name_plural": "historical EuroQol EQ-5D-3L Instrument",
            },
        ),
        migrations.AlterModelOptions(
            name="historicalsf12",
            options={
                "get_latest_by": ("history_date", "history_id"),
                "ordering": ("-history_date", "-history_id"),
                "verbose_name": "historical SF-12 Health Survey",
                "verbose_name_plural": "historical SF-12 Health Survey",
            },
        ),
        migrations.AlterField(
            model_name="historicaleq5d3l",
            name="history_date",
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name="historicalsf12",
            name="history_date",
            field=models.DateTimeField(db_index=True),
        ),
    ]