# Generated by Django 3.0.2 on 2020-04-09 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gazette', '0015_auto_20200409_1536'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auteur', models.CharField(max_length=200)),
                ('commentaire', models.TextField()),
                ('pub_date', models.DateTimeField(verbose_name='date de publication')),
                ('larticle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gazette.Article')),
            ],
        ),
    ]
