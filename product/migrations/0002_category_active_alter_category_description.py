# Generated by Django 5.1.1 on 2024-09-17 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="active",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="category",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
    ]
