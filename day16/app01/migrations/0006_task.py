# Generated by Django 4.1.7 on 2023-04-14 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app01", "0005_admin"),
    ]

    operations = [
        migrations.CreateModel(
            name="Task",
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
                (
                    "level_choices",
                    models.SmallIntegerField(
                        choices=[(1, "紧急"), (2, "重要"), (3, "临时")],
                        default=1,
                        verbose_name="级别",
                    ),
                ),
                ("title", models.CharField(max_length=64, verbose_name="标题")),
                ("detail", models.TextField(verbose_name="任务详细信息")),
            ],
        ),
    ]
