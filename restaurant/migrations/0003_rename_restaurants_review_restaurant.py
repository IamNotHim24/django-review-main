# Generated by Django 4.0.10 on 2023-02-28 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='restaurants',
            new_name='restaurant',
        ),
    ]