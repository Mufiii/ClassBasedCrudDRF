# Generated by Django 4.2.5 on 2023-09-11 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Football',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.CharField(max_length=150)),
                ('player', models.CharField(max_length=150)),
                ('jersey_no', models.IntegerField()),
            ],
        ),
    ]