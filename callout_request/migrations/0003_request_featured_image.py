# Generated by Django 3.2.19 on 2023-05-29 12:49

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callout_request', '0002_rename_post_comment_request'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]