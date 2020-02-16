# Generated by Django 3.0.3 on 2020-02-16 19:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("description", models.TextField()),
                ("frequency_in_days", models.IntegerField()),
                ("email", models.CharField(blank=True, max_length=100, null=True)),
                ("linkedin_url", models.CharField(blank=True, max_length=100, null=True)),
                ("twitter_username", models.CharField(blank=True, max_length=50, null=True)),
                ("phone_number", models.TextField(blank=True, max_length=50, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Touchpoint",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("when", models.DateTimeField()),
                (
                    "contact",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="networking_base.Contact"
                    ),
                ),
            ],
        ),
    ]
