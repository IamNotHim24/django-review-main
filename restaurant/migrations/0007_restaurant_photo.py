# Generated by Django 4.0.10 on 2024-11-24 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0006_rename_username_review_author_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='restaurant_photos/'),
        ),
    ]
