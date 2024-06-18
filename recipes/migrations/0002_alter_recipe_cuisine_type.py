# Generated by Django 4.2.13 on 2024-06-16 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="cuisine_type",
            field=models.CharField(
                choices=[
                    ("other", "Other"),
                    ("african", "African"),
                    ("americana", "Americana"),
                    ("asian", "Asian"),
                    ("chinese", "Chinese"),
                    ("indian", "Indian"),
                    ("italian", "Italian"),
                ],
                default="Other",
                max_length=50,
            ),
        ),
    ]
