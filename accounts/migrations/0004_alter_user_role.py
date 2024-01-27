# Generated by Django 5.0 on 2024-01-26 10:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0003_user_country_user_nationality_alter_user_role_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="role",
            field=models.PositiveBigIntegerField(
                blank=True,
                choices=[(1, "Student"), (2, "Staff"), (3, "Admin"), (4, "Editor")],
                default=1,
                null=True,
            ),
        ),
    ]
