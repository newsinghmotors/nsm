# Generated by Django 4.2.3 on 2024-02-28 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("feed", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="keys",
            name="madin",
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name="keys",
            name="minda",
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name="keys",
            name="saran",
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
