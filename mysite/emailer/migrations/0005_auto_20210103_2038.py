# Generated by Django 3.1.4 on 2021-01-03 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emailer', '0004_auto_20210103_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='correct_choice',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]