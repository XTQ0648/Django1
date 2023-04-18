# Generated by Django 4.1.7 on 2023-04-07 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app01", "0003_userinfo_field"),
    ]

    operations = [
        migrations.RemoveField(model_name="userinfo", name="field",),
        migrations.AddField(
            model_name="userinfo",
            name="size",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="userinfo", name="age", field=models.IntegerField(default=2),
        ),
    ]