# Generated by Django 3.1.4 on 2020-12-27 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendee',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]
