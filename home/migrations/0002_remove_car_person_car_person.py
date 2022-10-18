# Generated by Django 4.1.2 on 2022-10-18 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="car",
            name="person",
        ),
        migrations.AddField(
            model_name="car",
            name="person",
            field=models.ManyToManyField(related_name="cars", to="home.person"),
        ),
    ]