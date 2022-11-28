# Generated by Django 4.1.3 on 2022-11-28 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Password",
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
                ("title", models.CharField(max_length=50, verbose_name="عنوان")),
                ("url", models.URLField(verbose_name="مسیر")),
                ("password", models.CharField(max_length=225, verbose_name="رمز عبور")),
                ("username", models.CharField(max_length=50, verbose_name="نام")),
                (
                    "description",
                    models.TextField(
                        blank=True, max_length=200, null=True, verbose_name="توضیحات"
                    ),
                ),
            ],
        ),
    ]