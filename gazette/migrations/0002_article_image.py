# Generated by Django 3.0.2 on 2020-03-27 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gazette', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.FileField(blank=True, upload_to='image_publie'),
        ),
    ]
