# Generated by Django 4.2.4 on 2023-08-09 16:59

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Phone",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=50)),
                ("image", models.CharField()),
                ("price", models.IntegerField()),
                ("release_date", models.DateField()),
                ("lte_exist", models.BooleanField()),
                ("slug", models.SlugField(unique=True)),
            ],
        ),
    ]