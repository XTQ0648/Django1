# Generated by Django 4.1.7 on 2023-04-10 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app01", "0002_alter_userinfo_depart"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userinfo",
            name="create_time",
            field=models.DateTimeField(default=2018, verbose_name="入职时间"),
        ),
    ]