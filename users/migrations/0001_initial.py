# Generated by Django 4.1.5 on 2023-01-08 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Location",
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
                ("name", models.CharField(max_length=50)),
                ("lat", models.DecimalField(decimal_places=6, max_digits=8, null=True)),
                ("lng", models.DecimalField(decimal_places=6, max_digits=8, null=True)),
            ],
            options={
                "verbose_name": "Локация",
                "verbose_name_plural": "Локации",
            },
        ),
        migrations.CreateModel(
            name="User",
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
                ("first_name", models.CharField(max_length=20, null=True)),
                ("last_name", models.CharField(blank=True, max_length=20, null=True)),
                ("username", models.CharField(max_length=20, unique=True)),
                ("password", models.CharField(max_length=20)),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("member", "пользователь"),
                            ("admin", "администратор"),
                            ("moderator", "модератор"),
                        ],
                        default="member",
                        max_length=9,
                    ),
                ),
                ("age", models.PositiveSmallIntegerField()),
                ("location", models.ManyToManyField(to="users.location")),
            ],
            options={
                "verbose_name": "Пользователь",
                "verbose_name_plural": "Пользователи",
            },
        ),
    ]