# Generated by Django 3.0.2 on 2020-03-27 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gazette', '0003_auto_20200327_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, upload_to='image_publie/'),
        ),
    ]
