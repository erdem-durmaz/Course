# Generated by Django 3.1.4 on 2021-01-03 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emailer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=250)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emailer.question')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emailer.quiz')),
            ],
        ),
    ]